HOST = '10.0.0.1'

from constantes_tcp import *
import socket, sys

conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexão.connect((HOST,PORT))
while True:
    print('-'*100)
    try:    
        nome_arq = input('Digite o nome do arquivo (EXIT p/ sair):');print('-'*100)
        conexão.sendall(nome_arq.encode(CODE_PAGE))
        print('-'*100)
        if nome_arq.upper() == 'EXIT':
            print('Fechando a conexão.')
            conexão.close()
            break
    except:
        print(f'Erro de conexão... {sys.exc_info()[0]}')
        dado_retorno, ip_retorno = conexão.recvfrom(BUFFER)
        dado_retorno = dado_retorno.decode(CODE_PAGE)
        if 'Size:' in dado_retorno:
            tamanho = int(dado_retorno.split(':')[-1])
        
        try: 
            print(f'Gravando o arquivo {nome_arq} ({tamanho} bytes)')
            nome_arq = DIR_ATUAL + '\\img_client\\' + nome_arq
            arquivo = open(nome_arq, 'wb')
        except:
            print(f'Erro ao salvar o arquivo... {sys.exc_info()[0]}')

        bytes_recebidos = 0
        pct = 1
        while True:
            try:
                dado_retorno, ip_retorno = conexão.recvfrom(BUFFER) #Definindo a mensagem recebida e o IP do servidor que está sendo conectado
                if not dado_retorno: break #Finalizando o laço se não possuir dados
                print(f'Pacote ({pct}) - Dados Recebidos: {len(dado_retorno)} bytes')
            except:
                print(f'Erro ao obter o retorno do servidor... {sys.exc_info()[0]}.')
            try:
                arquivo.write(dado_retorno)
                bytes_recebidos += len(dado_retorno)
                if bytes_recebidos >= tamanho: break
                pct += 1
            except:
                print(f'Erro ao calcular is dados de retorno... {sys.exc_info()[0]}')
            arquivo.close()

# Fechando o socket
conexão.close()  