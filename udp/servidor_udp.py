import socket
import random

HOST = "127.0.0.1"
PORTA = 1232

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((HOST, PORTA))

print("Servidor UDP esperando mensagem...")

numero_secreto = random.randint(1, 11)

while True:
    mensagem, endereco = servidor.recvfrom(1024)

    print("Cliente:", endereco)

    mensagem = mensagem.decode()

    print("Palpite recebido:", mensagem)

    palpite = int(mensagem)

    if palpite == numero_secreto:
        resposta = "Acertou"
        servidor.sendto(resposta.encode(), endereco)
        break

    else:
        resposta = "Errou! Tente novamente."
        servidor.sendto(resposta.encode(), endereco)

servidor.close()  