import threading, os, sys
local = os.path.dirname(os.path.abspath(__file__)) + '\\Functions_and_Var'
sys.path.append(local)
from variables import *
from server_func import *
from client_func import *


try: # Tentando estabelecer a conexão
    server = conn_server()
    clients = {} #Criando o dicionário onde ficaram armazenados os clientes conectados
    while True:
        try:
            sock_client, end = server.accept()#Aceitando  as conexões
            PRINTS(f'Conexão TCP estabelecida.\n\nCliente {end[0]} conectado na porta {end[1]}.')
            clients[end[1]] = [end[0], sock_client] #Inserindo no dicionário a PORTA:IP do cliente
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