import os

HOST_SERVER = 'localhost'   # Definindo o IP do servidor
SOCKET_PORT = 50000         # Definindo a porta
CODE_PAGE   = 'utf-8'       # Definindo a página de códigos de caracteres-

BUFFER_SIZE = 512           # Definindo o tamanho do buffer de envio

MAX_LISTEN  = 1             # Definindo o máximo de conexões enfileiradas 

DIR_ATUAL = os.path.dirname(os.path.abspath(__file__))