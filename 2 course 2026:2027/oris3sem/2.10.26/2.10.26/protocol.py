import struct # небольшой дисклеймер, в файлах вы можете увидеть что вместо JOIN я использовал JOINUSER, я так проверял работает ли возможность указывать команду любой длинны.

COMMAND_SIZE = 64 # здесь мы заменили 4 на 64 так как в самом задании указано что нужно поставить так или иначе лимит, что бы чел не написал команду длинною в мегабайт
HEADER_FORMAT = "!II" # туть по факту то по чему мы можем отправлять команды разные по длинне, т.е после ! первая I означает длину команды а вторая уже длинну payload, в функциях сенд и ресив мы сможем основываясь на этих длинах уже высчитать точноее кол-во байт для той или иной команды
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
MAX_MESSAGE_SIZE = 10 * 1024 * 1024


def recv_exact(sock, size):
    chunks = bytearray()
    while len(chunks) < size:
        chunk = sock.recv(size - len(chunks))
        if not chunk:
            raise ConnectionError("соединение закрыто до получения всех данных")
        chunks.extend(chunk)
    return bytes(chunks)


def send_message(sock, command, payload=b""):
    if len(payload) > MAX_MESSAGE_SIZE:
        raise ValueError(f"payload слишком большой: {len(payload)} байт")
    command_bytes = command.encode("utf-8") # заменили ascii на utf-8 так как в задании указано что нужно использовать именно utf-8
    header = struct.pack(HEADER_FORMAT, len(command_bytes), len(payload)) # тут мы теперь заместо просто комманд_байтс берем длинну комманд_байтсов, так как именно она и передается в хедере
    sock.sendall(header + command_bytes + payload) # тут мы помимо хедера и пейлоада отправляем еще и команд_байтс из за того что строчкой выше теперь мы имеем дело с длинной команд_байтс а не с самими байтами а значит нам нужно их отправить отдельно


def recv_message(sock):
    try:
        header = recv_exact(sock, HEADER_SIZE)
    except ConnectionError:
        return None
    command_length, length = struct.unpack(HEADER_FORMAT, header) # тут вместо комманд_байтс комманд_ленгх, так как мы уже не знаем сколько байт нам нужно прочитать, но зная длинну команды мы можем прочитать именно столько байт сколько нужно.
    if not 0 < command_length <= COMMAND_SIZE: # здесь простая проверка на то что комманда соотвествует или не соответсвует лимиту
        raise ValueError(f"заявленная длина команды {command_length} несоответствует лимиту") 
    command_bytes = recv_exact(sock, command_length) # тут уже мы наконец читаем сколько байт нам нужно
    command = command_bytes.decode("utf-8")
    payload = recv_exact(sock, length) if length else b""
    return command, payload

