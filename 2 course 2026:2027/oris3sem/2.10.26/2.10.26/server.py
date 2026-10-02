import socket
import threading
import protocol as proto
import logging # это нужно для логирования. если честно я не понял что именно в задании указано как лог демонстрации поэтому посоветовался с иишкой, тот в свою очередь посоветовал мне использовать этот модуль. по факту этот модул сам ничего не делает кроме как пишет в файлик, надеюсь что за совет с иишкой именно ПО ЭТОМУ вопросу проблем не будет...
from pathlib import Path # тут патлиб тоже нужен для логирования. также кстати небольшой дисклеймер, в файлах вы можете увидеть что вместо JOIN я использовал JOINUSER, я так проверял работает ли возможность указывать команду любой длинны.

HOST = "0.0.0.0"
PORT = 5555

PROJECT_DIR = Path(__file__).resolve().parent.parent # эта строчка и с 12 по 18 указания папки для сохранения логов и конфиг.

logging.basicConfig(
    filename=str(PROJECT_DIR / "client.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

clients = {}
clients_lock = threading.Lock()


def broadcast(command, text, exclude=None):
    payload = text.encode("utf-8")
    with clients_lock:
        targets = [s for s in clients if s is not exclude]
    for sock in targets:
        try:
            proto.send_message(sock, command, payload)
        except (BrokenPipeError, ConnectionResetError, OSError):
            pass


def handle_client(sock, addr):
    username = None
    try:
        first = proto.recv_message(sock)
        if first is None or first[0] != "JOINUSER":
            proto.send_message(sock, "ERROR", b"first command must be JOINUSER")
            logging.warning(f"{addr} - invalid first command: {first}")
            return

        username = first[1].decode("utf-8", errors="replace").strip()
        with clients_lock: 
            if not username or username in clients.values():
                proto.send_message(sock, "ERROR", b"invalid or taken username")
                logging.warning(f"{addr} - invalid or taken username: {username}")
                return
            clients[sock] = username

        proto.send_message(sock, "TEXT", f"* вы вошли как {username}".encode())
        broadcast("TEXT", f"* {username} присоединился", exclude=sock)
        print(f"[+] {username} присоединился ({addr})")
        logging.info(f"{username} ({addr}) присоединился")

        while True:
            msg = proto.recv_message(sock)
            if msg is None:
                print(f"[i] {username} отключился без QUIT")
                logging.info(f"{username} ({addr}) отключился без QUIT")
                break

            command, payload = msg
            if command == "TEXT":
                text = payload.decode("utf-8", errors="replace")
                broadcast("TEXT", f"{username}: {text}", exclude=sock)
            elif command == "LIST":
                with clients_lock:
                    names = list(clients.values())
                proto.send_message(sock, "LIST", "\n".join(names).encode())
            elif command == "QUIT":
                proto.send_message(sock, "TEXT", b"* bye")
                print(f"[-] {username} вышел через QUIT")
                logging.info(f"{username} ({addr}) вышел через QUIT")
                break
            elif command == "NICK": # ниже идет прием нового юзернейма, проверку я тактично скопипастил с самого первого юзернейма, так как логика такая же
                new_username = payload.decode("utf-8").strip() # тоже кстати важная строчка, тут мы принимаем и декодируем новый юзернейм 
                with clients_lock: 
                    if not new_username or new_username in clients.values():
                        proto.send_message(sock, "ERROR", b"invalid or taken username")
                        logging.warning(f"{username} ({addr}) tried to change to invalid or taken username: {new_username}")
                        continue # тут вместо брейк, континью так как разрывать соединение не нужно, просто чел должен ввести другое имя а не переподключаться к серверу
                    old_username = clients[sock] # тут мы должны сохранить старый юзернейм, дабы сделать уведомление о том с какого юзернейма на какой чел пересел. вообще это можно было и не делать, но я подумал что в таком случае будет выглядеть слишком сыро
                    clients[sock] = new_username # тут мы уже добавляем новый юзернейм, так же что бы сделать уведомление и переназначить его в переменной ниже
                broadcast("TEXT", f"* {old_username} сменил имя на {new_username}")
                username = new_username 
                print(f"[i] {old_username} сменил имя на {new_username}")
                logging.info(f"{old_username} ({addr}) сменил имя на {new_username}")
            else:
                proto.send_message(sock, "ERROR", f"unknown command {command}".encode())

    except ConnectionResetError:
        print(f"[!] {username or addr} - соединение сброшено (RST)")
    except BrokenPipeError:
        print(f"[!] {username or addr} - не удалось отправить, соединение разорвано")
    finally:
        with clients_lock:
            clients.pop(sock, None)
        sock.close()
        if username:
            broadcast("TEXT", f"* {username} покинул чат")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"[*] сервер слушает {HOST}:{PORT}")
        while True:
            client_sock, addr = server.accept()
            threading.Thread(target=handle_client, args=(client_sock, addr), daemon=True).start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] сервер остановлен")
        
