from Functions_and_Var import *
import socket, threading

try:
    clients_list = {}
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))

    print ("Servidor ativo: ", (SERVER, PORT))
    sock.listen(5)

    while True:
        socket_client, client_info = sock.accept()

        print (client_info,'Se conectou ao servidor.')
        clients_list[client_info[1]] = [client_info[0], socket_client] #Inserindo no dicionário a PORTA:IP do cliente
        tClient = threading.Thread(target=Client_Interaction, args=(socket_client, client_info, clients_list))

        tClient.start()

except Exception as e:
    print ("Fail: ", e)