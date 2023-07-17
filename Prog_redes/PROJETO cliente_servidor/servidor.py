import socket, threading, os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Var')
from variables import *
from functions_client import *
from functions_others import PRINT_DIV


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
        ()
            
except OSError as e:
    if e.errno == 98:
        print('Todas as portas do servidor estão ocupadas')
    else:
        print('Erro ao estabelecer a conexão do servidor:', e)