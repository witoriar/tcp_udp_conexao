Comunicação TCP e UDP

Este projeto foi desenvolvido para estudar e demonstrar a comunicação entre cliente e servidor utilizando os protocolos TCP e UDP em Python.
O projeto possui duas aplicações:
• TCP: conversão de valores de Real para Dólar.
• UDP: jogo de adivinhação de números.


TCP
Na aplicação TCP, o cliente envia um valor em reais para o servidor.
O servidor recebe o valor, realiza uma conversão para dólar utilizando uma cotação definida no código e envia o resultado de volta para o cliente.

Fluxo de comunicação:
Cliente TCP
     |
     | valor em reais
     |
Servidor TCP
     |
     | realiza a conversão
     |
Cliente TCP
     |
     | resultado em dólares 

O TCP é orientado à conexão, o cliente estabelece uma conexão com o servidor,
No projeto, isso pode ser observado pelas funções:
connect() listen() accept()

UDP
Na aplicação UDP foi desenvolvido um jogo de adivinhação.
O servidor escolhe aleatoriamente um número entre 1 e 11.
O cliente tenta descobrir qual é o número enviando seus palpites para o servidor.

Fluxo de comunicação:
Cliente UDP
     |
     | envia palpite
     |
Servidor UDP
     |
     | verifica o número
     |
Cliente UDP
     |
     | recebe a resposta
     |
  continua tentando

O UDP não estabelece uma conexão como o TCP, as mensagens são enviadas diretamente utilizando:
sendto() recvfrom()

Sockets
Os dois programas utilizam sockets Python para realizar a comunicação.

No TCP: 
socket.socket(socket.AF_INET, socket.SOCK_STREAM)

No UDP:
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

Tecnologias utilizadas:
• Python
• Sockets
• TCP
• UDP
• IPv4
• Git
• GitHub
