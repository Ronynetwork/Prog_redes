import threading, socket
from constantes import *

server, conn, end = connm_server()
try:
    clients = []
    while True:  
        conn_server, end = server.accept()
        print ("Connection from: ", end)
        clients.append((conn_server, end))
        tClient = threading.Thread(target=Client_Interaction(), args=(conn_server, end))
        tClient.start()
except:
    print('Todas as portas do servidor estão ocupadas')