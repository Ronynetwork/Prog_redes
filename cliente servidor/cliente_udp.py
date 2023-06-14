import socket, sys
from server_constantes import *

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicitar o arquivo
    nome_arquivo = input('Digite o nome do arquivo (EXIT p/ sair):') # Solicitando o arquivo a ser baixado
    
    # Enviando o nome do arquivo para o servidor
    print(f'\nSolicitando o arquivo {nome_arquivo}')
    udp_socket.sendto(nome_arquivo.encode(CODE_PAGE), (HOST_SERVER, SOCKET_PORT))#Enviando a  requisição do arquivo para o servidor 
    
    if nome_arquivo.upper() == 'EXIT': break #Quebrando a conexão caso o cliente digite EXIT

    # Recebendo o conteúdo do servidor
    dado_retorno, ip_retorno = udp_socket.recvfrom(BUFFER_SIZE) # Recebendo do servidor o dado de retorno e ip de retorno

    # Gravar o dado recebido em arquivo
    print(f'Gravando o arquivo {nome_arquivo}') 
    try:
        with open (nome_arquivo, 'wb') as arquivo:
            arquivo.write(dado_retorno)
    except:
        print(f'Erro ao salvar o arquivo...{sys.exc_info()[0]}');print('-'*100)
        exit()
# Fechando o socket
udp_socket.close()