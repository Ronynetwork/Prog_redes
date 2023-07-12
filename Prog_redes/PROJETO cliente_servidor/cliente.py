from constantes import *
import threading

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))
    print ("Conectado a: ", (SERVER, PORT))
    tServer = threading.Thread(target=server_interaction(sock))
    tUser = threading.Thread(target=client_interaction(sock))

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()

except Exception as e:
    print ("Falha ", e)
