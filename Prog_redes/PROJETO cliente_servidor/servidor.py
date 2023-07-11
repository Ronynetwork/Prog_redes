import threading, socket
from constantes import *

SERVER = '0.0.0.0'
PORT = 7000

try:
    server, conn, end = conn_server()
    clients = []
    while True:  
        end = server.accept()
        print ("Connection from: ", end)
        clients.append((conn_server, end))
        tClient = threading.Thread(target=Client_Interaction(), args=(conn, end))
        tClient.start()
except:
    print('Todas as portas do servidor estão ocupadas')