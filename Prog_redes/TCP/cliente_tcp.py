import socket, time, sys

from funcoes import *

client = CONEXÃO_CLIENTE()

past = PAST_CLIENT()
print(past)
try: 
    while True:
# Solicitar o arquivo
        arq_solicitado = input('Digite o arquivo que deseja baixar do servidor (Ou EXIT para sair):')

        # Enviando o nome do arquivo para o servidor
        PRINTS(f'\nSolicitando o arquivo {arq_solicitado}')
        
        client.send(arq_solicitado.encode())

        if (arq_solicitado).lower() == 'exit': 
            client.send(arq_solicitado.encode())
            print('Você solicitou o fim da conexão.\n\nAté a próxima!!')
            print('-'*100)
            break
        check = eval(client.recv(4096).decode())
        tamanho = check[1]
        print(check[0])
        if check[0] == True:
            qtd_pct_total = int(tamanho)//4096
            pct = 0
            print('chegou aqui')
            data_retorno = 0
            total_retorno = 0
            print('arquivo criado')
            arquivo = open(check[3],'wb')
            while True:
                data_retorno = client.recv(4096)
                total_retorno += len(data_retorno)
                print(len(total_retorno))
                arquivo.write(data_retorno)
                             
except:
    print('sla')
'''
        data_retorno = 0
        while True:
            data_retorno += (client.recv(4096).decode())
            if not data_retorno:
                break
            print(len(data_retorno))
        tamanho_total, qtd_pacotes = DADOS(data_retorno)

        try:
            nome_arq = past + arq_solicitado
            arquivo = open(nome_arq, 'wb')
        except:
            print(f'Erro ao salvar o arquivo... {sys.exc_info()[0]}')
            
        PACOTES(client, arquivo, tamanho_total, qtd_pacotes)
except:
    print(f'Erro... {sys.exc_info()[0]}')
client.close()'''