from funcoes import *

dir_atual = os.path.dirname(os.path.abspath(__file__))
conn, end,server = CONEXÃO_SERVER()

try:
    arq_existe = 0
    while True:
        mensagem = conn.recv(512)
        mensagem = mensagem.decode('utf-8')

        if mensagem.lower() == 'exit':
            print(f'\nO {end} SE DESCONECTOU DO SERVIDOR...\n')
            conn.close()
            server.close()    
            break

        else:
            nome_arquivo = dir_atual + '\\img_server\\' + mensagem
            print(nome_arquivo)
            lista = os.listdir(dir_atual + '\\img_server\\')
            for arquivo in lista:
                print(arquivo)
                if nome_arquivo != arquivo:
                    arq_existe = 1
            if arq_existe == 1:
                print(f'O Arquivo que você pediu {mensagem} não existe no servidor!')
                
            total_data = 0
            try:
                print('Deu certo porra')


                size_arq = os.path.getsize(nome_arquivo)
                print(size_arq)
                comunicacao = (f'Size:{size_arq}')
                conn.send(comunicacao.encode('utf_8'))



                with open(nome_arquivo, 'rb') as arquivo:
                    while True:
                        data_retorno = arquivo.read(4096)
                        if not data_retorno:
                            break
                        total_data += len(data_retorno)
                        print(total_data)
                        conn.send(data_retorno)
                        
            except:
                print('Não foi possivel enviar o restante do arquivo')

except FileNotFoundError:
    conn.send('O arquivo não existe nossa base de dados.'.encode())