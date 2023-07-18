import threading, os, sys
local = os.path.dirname(os.path.abspath(__file__)) + '\\Functions_and_Var'
sys.path.append(local)
from variables import *
from server_func import *
from client_func import *


try: # Tentando estabelecer a conexão
    clients = {} #Criando o dicionário onde ficaram armazenados os clientes conectados
    server = conn_server(clients)
    while True:
        try:
            sock_client, client_info = server.accept()#Aceitando  as conexões
            PRINTS(f'Conexão TCP estabelecida.\n\nCliente {client_info[0]} | Porta: {client_info[1]}.')
            clients[client_info[1]] = [client_info[0], sock_client] #Inserindo no dicionário a PORTA:IP do cliente
            tClient = threading.Thread(target=Client_Interaction, args=(sock_client, client_info, clients))
            tClient.start()
        except:
            print(f'Erro ao estabelecer a conexão... {sys.exc_info()[0]}')
            exit()
except OSError as e:
    if e.errno == 98:
        print('Todas as portas do servidor estão ocupadas')
    else:
        print('Erro ao estabelecer a conexão do servidor:', e)