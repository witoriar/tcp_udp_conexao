import socket

HOST = "127.0.0.1"
PORTA = 1232

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor.bind((HOST, PORTA))

print("Servidor UDP esperando mensagem...")

mensagem, endereco = servidor.recvfrom(1024)

print("Cliente:", endereco)
mensagem = mensagem.decode().upper()
print("Mensagem recebida:", mensagem)


resposta = f"Mensagem recebida pelo servidor UDP: {mensagem}"
servidor.sendto(resposta.encode(), endereco)

servidor.close()
