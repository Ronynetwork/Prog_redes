import socket, sys
from server_constantes import *

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicitar o arquivo
    print('-'*100)
    nome_arquivo = input('Digite o nome do arquivo (EXIT p/ sair):');print('-'*100) # Solicitando o arquivo a ser baixado

    # Enviando o nome do arquivo para o servidor
    print(f'Solicitando o arquivo {nome_arquivo}');print('-'*100)

    udp_socket.sendto(nome_arquivo.encode(CODE_PAGE), (HOST_SERVER, SOCKET_PORT))#Enviando a  requisição do arquivo para o servidor 
    
    if nome_arquivo.upper() == 'EXIT': break #Quebrando a conexão caso o cliente digite EXIT

    # Recebendo o conteúdo do servidor
    dado_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE) # Recebendo do servidor o dado de retorno e ip de retorno
    dado_retorno = dado_retorno.decode(CODE_PAGE) #Deixando o arquivo legível

    if 'Size:' in dado_retorno:
        total_lenght = int(dado_retorno.split(':')[1])

    # Gravar o dado recebido em arquivo
    print(f'Gravando o arquivo {nome_arquivo} ({total_lenght} bytes)')
    nome_arquivo_ = DIR_ATUAL + '\\img_client\\' + nome_arquivo
    arquivo = open(nome_arquivo_, 'wb')
    bytes_recebidos = 0
    pct = 1

    while True:
        # Recebendo o conteúdo do servidor
        dado_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE) #Definindo a mensagem recebida e o IP do servidor que está sendo conectado
        if not dado_retorno: break #Finalizando o laço se não possuir dados
        print(f'Pacote ({pct}) - Dados Recebidos: {len(dado_retorno)} bytes')
        
        arquivo.write(dado_retorno)
        bytes_recebidos += len(dado_retorno)
        if bytes_recebidos >= total_lenght: break
        pct += 1
# Fechando o socket
udp_socket.close()  