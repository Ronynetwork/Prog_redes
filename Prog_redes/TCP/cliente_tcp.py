import socket, time, sys

from funcoes import *

client = CONEXÃO_CLIENTE()

past = PAST_CLIENT()

try: 
    while True:
# Solicitar o arquivo
        arq_solicitado = input('Digite o arquivo que deseja baixar do servidor (Ou EXIT para sair):')

        # Enviando o nome do arquivo para o servidor
        print(f'\nSolicitando o arquivo {arq_solicitado}')
        print('-'*100)
        client.send(arq_solicitado.encode())

        if (arq_solicitado).lower() == 'exit': 
            client.send(arq_solicitado.encode())
            print('Você solicitou o fim da conexão.\n\nAté a próxima!!')
            print('-'*100)
            break

        dado_retorno = (client.recv(8192).decode())

        tamanho_total, qtd_pacotes = DADOS(dado_retorno)

        try:
            nome_arq = past + arq_solicitado
            arquivo = open(nome_arq, 'wb')
        except:
            print(f'Erro ao salvar o arquivo... {sys.exc_info()[0]}')
            
        PACOTES(client, arquivo, tamanho_total, qtd_pacotes)
except:
    print(f'Erro... {sys.exc_info()[0]}')
client.close()