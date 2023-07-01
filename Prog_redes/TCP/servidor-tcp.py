from funcoes import *

conn, end,server = CONEXÃO_SERVER()

try:
    while True:
        mensagem = conn.recv(11264).decode('utf-8')

        if mensagem.lower() == 'exit':
                print(f'\nO {end} SE DESCONECTOU DO SERVIDOR...\n')
                break
        ENV_ARQ(conn,mensagem)

except FileNotFoundError:
    conn.send('O arquivo não existeem nossa base de dados')

finally:
    conn.close()
    server.close()