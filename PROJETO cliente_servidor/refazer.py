from Functions_and_Var import *
import socket, threading

try:
    server = conn_server()
    clients_list = {}
    while True:
        socket_client, client_info = server.accept()

        PRINTS (f'{client_info} Se conectou ao servidor.'); print('-'*100)
        clients_list[client_info[1]] = [client_info[0], socket_client] #Inserindo no dicionário a PORTA:IP do cliente
        tClient = threading.Thread(target=Client_Interaction, args=(socket_client, client_info, clients_list))

        tClient.start()

except Exception as e:
    print ("Fail: ", e)