import threading, socket
from constantes import *


try:
    server = conn_server()
    clients = []

    while True:  
        sock_client, end = server.accept()
        PRINTS(f'\nConexão TCP estabelecida.\nCliente {end[0]} conectado na porta {end[1]}.')
        print ("Connection from: ", end)
        clients.append((conn_server, end))
        tClient = threading.Thread(target=Client_Interaction, args=(sock_client, end))
        tClient.start()

except Exception as e:
    if e.errno == 98:
        print('Todas as portas do servidor estão ocupadas')
    else:
        print('Erro ao estabelecer a conexão do servidor:', e)