from funcoes import *

dir_img = os.path.dirname(__file__)

conn, end,server = CONEXÃO_SERVER()

try:
    while True:
        mensagem = (conn.recv(4096)).decode()

        if mensagem.lower() == 'exit':
            print(f'\nO {end} SE DESCONECTOU DO SERVIDOR...\n')
            conn.close()
            server.close()    
            break
        else:
            check = CHECAGEM(mensagem)
            print(check)
            if check[0] == True:
                total_data = 0
                conn.send(str(check).encode())

                print('Deu certo porra')
                with open(check[2], 'rb') as arquivo:
                    while True:
                        data_retorno = arquivo.read(4096)
                        total_data += len(data_retorno)
                        print(total_data)
                        conn.send(data_retorno)
                        if not data_retorno:
                            break

except FileNotFoundError:
    conn.send('O arquivo não existe nossa base de dados.'.encode())
'''try:
    if check[0] == True:
        total_data_retorno = 0
        arquivo = open(check[2], 'rb')
        try:
            while True:
                data_retorno = arquivo.read(4096)
                total_data_retorno += len(data_retorno)
                conn.send(data_retorno)
                print(len(total_data_retorno))
                if not data_retorno:
                    break
        except:
            print(f'Erro no envio dos bytes do arquivo ... {sys.exc_info()[0]}')
    else:
        conn.send(str(check).encode())'''