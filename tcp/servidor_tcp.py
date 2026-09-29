import socket

HOST = "127.0.0.1"
PORTA = 1232

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor.bind((HOST, PORTA))
servidor.listen(1)

print("Servidor TCP esperando conexão...")

conexao, endereco = servidor.accept()

print("Cliente conectado:", endereco)

mensagem = conexao.recv(1024)
mensagem = mensagem.decode()

print("Mensagem recebida:", mensagem)


resposta = f"Mensagem recebida pelo servidor TCP: {mensagem}"
conexao.send(resposta.encode())

conexao.close()
servidor.close()

