from funcoes import *

dir_img = os.path.dirname(__file__)

conn, end,server = CONEXÃO_SERVER()

try:
    while True:
        mensagem = (conn.recv(8192)).decode()

        if mensagem.lower() == 'exit':
            print(f'\nO {end} SE DESCONECTOU DO SERVIDOR...\n')
            conn.close()
            server.close()    
            break

        check = CHECAGEM(mensagem, dir_img)

        if check[0] == False:
            conn.send(str(check).encode())

        else:
            total_data_retorno = 0
            with open(check[2], 'rb') as arquivo:
                while True:
                    data_retorno = arquivo.read(8192)
                    total_data_retorno += len(data_retorno)
                    conn.send(data_retorno)
                    if not data_retorno:
                        break
except FileNotFoundError:
    conn.send('O arquivo não existe nossa base de dados.'.encode())

finally:
    conn.close()
    server.close()