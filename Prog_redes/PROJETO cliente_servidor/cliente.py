import threading, os, sys, 
local = os.path.dirname(os.path.abspath(__file__)) + '\\Functions_and_Var'
sys.path.append(local)

from variables import *
from client_func import *




try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((CLIENT, PORT))
    PRINTS (f'Conectado ao cliente: {SERVER}, na porta {PORT}')
    tServer = threading.Thread(target=server_interaction, args=(sock,))
    tUser = threading.Thread(target=client_interaction, args=(sock,))

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
except: 
    print(f'Falha na conexão com o servidor... {sys.exc_info()[0]}')