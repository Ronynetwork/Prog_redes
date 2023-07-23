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

        if arq_solicitado.lower() == 'exit': 
            client.send(arq_solicitado.encode())
            print('Você solicitou o fim da conexão.\n\nAté a próxima!!')
            print('-'*100)
            break
        mensagem = client.recv(4096).decode()
        print(mensagem)
        if 'Size:' in mensagem:
            tamanho = int(mensagem.split(':')[1])
        
        qtd_pct_total = tamanho//4096
        pct = 0
        print('chegou aqui')
        total_retorno = 0
        print('arquivo criado')
        dir_arq = os.path.dirname(os.path.abspath(__file__)) + '\\img_client\\' + arq_solicitado
        arquivo = open(dir_arq,'wb')
        while True:
            data_retorno = client.recv(4096)
            if  not data_retorno:
                break
            total_retorno += len(data_retorno)
            print(len(total_retorno))
            arquivo.write(data_retorno)
            if total_retorno >= tamanho:
                break
        arquivo.close()
        print('O arquivo foi recebido com sucesso')
                             
except:
    print(f'Erro ... {sys.exc_info()}')