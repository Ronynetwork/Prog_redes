import threading, socket, sys, os
local = sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Var')
print(local)
from client_func import *

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((CLIENT, PORT))
    print (f'Conectado ao cliente: {SERVER}, na porta {PORT}')
    tServer = threading.Thread(target=server_interaction, args=(sock,))
    tUser = threading.Thread(target=client_interaction, args=(sock,))

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()

except Exception as e:
    print ("Falha ", e)