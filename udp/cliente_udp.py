import socket

HOST = "127.0.0.1"
PORTA = 1232

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Jogo de adivinhação")
print("Tente adivinhar um número de 1 a 11.")

while True:

    mensagem = input("Digite seu palpite: ")

    cliente.sendto(mensagem.encode(), (HOST, PORTA))

    resposta, endereco = cliente.recvfrom(1024)

    resposta = resposta.decode()

    print("Resposta do servidor:", resposta)

    if resposta == "Acertou":
        break

cliente.close()