import socket

HOST = "127.0.0.1"
PORTA = 1232
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mensagem = input("Digite uma mensagem:")

cliente.sendto(mensagem.encode(), (HOST, PORTA))

resposta, endereco = cliente.recvfrom(1024)

print("Resposta do servidor:", resposta.decode())

cliente.close()
