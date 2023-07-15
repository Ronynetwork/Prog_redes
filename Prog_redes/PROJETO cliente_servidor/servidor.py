import threading
from Functions_and_var import *

try:
    server = conn_server()
    clients = {}
    while True:
        try:
            sock_client, end = server.accept()
            PRINTS(f'Conexão TCP estabelecida.\n\nCliente {end[0]} conectado na porta {end[1]}.')
            clients[end[1]] = [end[0], sock_client]
            tClient = threading.Thread(target=Client_Interaction, args=(sock_client, end, clients))
            tClient.start()
        except:
            print(f'Erro ao estabelecer a conexão... {sys.exc_info()[0]}')
            exit()
            
except OSError as e:
    if e.errno == 98:
        print('Todas as portas do servidor estão ocupadas')
    else:
        print('Erro ao estabelecer a conexão do servidor:', e)