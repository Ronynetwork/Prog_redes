import threading, socket, sys, os
sys.path.append(os.path.abspath(__file__) + '\\Functions and Var')
import client_func

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