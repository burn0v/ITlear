import socket
import threading
import protocol as proto
import logging
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5555

PROJECT_DIR = Path(__file__).resolve().parent.parent

logging.basicConfig(
    filename=str(PROJECT_DIR / "client.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)


def listen_loop(sock, stop_event):
    while not stop_event.is_set():
        try:
            msg = proto.recv_message(sock)
        except (ConnectionResetError, OSError):
            msg = None
        if msg is None:
            print("\n[!] соединение с сервером потеряно")
            stop_event.set()
            break
        command, payload = msg
        text = payload.decode("utf-8", errors="replace")
        if command == "LIST":
            print(f"\n[пользователи онлайн]\n{text}\n> ", end="")
        elif command == "ERROR":
            print(f"\n[ошибка] {text}\n> ", end="")
        else:
            print(f"\n{text}\n> ", end="")


def main():
    usernames = {"username": None} # тут делаем словарь так как он изминяем и в него как раз таки можно добавить юзернейм из потока для таймаута
    input_event = threading.Event() # событие что бы мейн поток понял когда можно продолжить работу
    def timout_username(): # функция в которой мы или задаем юзернейм или нет (в таком случае он будет пустой строкой), в конце функциии мы все равно вызываем input_event.set() что бы мейн поток понял что можно продолжать работу
        try:
            usernames["username"] = input("Введите имя: ").strip()
        finally:
            input_event.set() 

    threading.Thread(target=timout_username, daemon=True).start() # деп поток, который отвечает за ввод юзернейма, работатет паралельно с мейн потоком

    if not input_event.wait(timeout=15): # тут устанавливается время таймаута, от которого зависит и функиця и поток, т.е. если чел не введет юзернейм за 15 секунд то сначало выполнится input_event.set() с пустым юзернеймом, доп. поток завершится и мы поймем что время то вышло, а так как мейну в любом случае нужен юзернейм, он возьмет пустую строку, в следствие чего прогрмама завершится так как юзернейм не корректен.
        print("Время ожидания истекло.")
        logging.warning("Время ожидания истекло.")
        return
    
    username = usernames["username"] # тут тупо ставим юзернейм который ввел чел в переменную


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
        proto.send_message(sock, "JOINUSER", username.encode())
    except (ConnectionRefusedError, OSError) as e:
        print(f"Не удалось подключиться: {e}")
        return

    stop_event = threading.Event()
    threading.Thread(target=listen_loop, args=(sock, stop_event), daemon=True).start()

    print("Команды: /list, /quit, /nick. Остальной текст - сообщение в чат.")
    try:
        while not stop_event.is_set():
            line = input("> ")
            if line == "/quit":
                proto.send_message(sock, "QUIT")
                break
            elif line == "/list":
                proto.send_message(sock, "LIST")
            elif line == "/nick":
                new_username = input("Введите новое имя:").strip() 
                if new_username:
                    proto.send_message(sock, "NICK", new_username.encode("utf-8"))
                else:
                    print("[!] имя не может быть пустым")
            elif line:
                proto.send_message(sock, "TEXT", line.encode())
    except (EOFError, KeyboardInterrupt, BrokenPipeError, OSError):
        pass
    finally:
        stop_event.set()
        sock.close()


if __name__ == "__main__":
    main()
