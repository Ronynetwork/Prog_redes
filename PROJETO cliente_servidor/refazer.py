from Functions_and_Var import *
import socket, threading

'''def cliInteraction(socket_client, client_info):
    comunicacao = b''
    while comunicacao != b'/q':
        try:
            comunicacao = socket_client.recv(512)
            broadCast (comunicacao, client_info)
        except:
            comunicacao = b'/q'
    print(f'O Usuário {client_info} se desconectou do servidor.')
    clients_list.remove ((socket_client, client_info))
    socket_client.close()

def broadCast(comunicacao, enderr): #Utilizando a mensagem recebida e o endereço do cliente como argumentos
    comunicacao = f"{enderr} -> {comunicacao.decode('utf-8')}" #
    print (comunicacao)
    for s_client, client_info in clients_list:
        if client_info != enderr:
            s_client.send(comunicacao.encode('utf-8'))'''

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