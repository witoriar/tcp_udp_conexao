import socket

HOST = "127.0.0.1"
PORTA = 1232

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORTA))

mensagem = input("Digite o valor em reais para conversão: ")

cliente.send(mensagem.encode())

resposta = cliente.recv(1024)

print("Resposta do servidor:", resposta.decode())

cliente.close()