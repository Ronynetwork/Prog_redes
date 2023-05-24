import socket, ssl, sys
import xml.etree.ElementTree as ET

# Constantes da Aplicação
# Solicitando o link da imagem a ser baixada:
link = input('Insira o link da imagem em que deseja realizar o download:')

# Separando em formato de lista com o método split:
link_separado = link.split('/')

# Utilizando a posição dos separadores para extrair o host:
conexão = link_separado[0]
url_host=link_separado[2]

# Unindo os elementos filtrados novamente em uma string:
url_image = '/'.join(link_separado[3:])
# Realizando a troca de extensão
extensão = link.split('.')[-1]
arq_img = link.replace(extensão,'txt')
print('-'*100);print(f'Seu host é ({url_host}).\nSua imagem é ({url_image}).');print('-'*100)

RSS_PORT     = 443
CODE_PAGE    = 'utf-8'
MAX_NOTICIAS = 10
BUFFER_SIZE  = 4096
# Construir requisição HTTP para obter o feed RSS
request  = f'GET {url_image} HTTP/1.1\r\n'
request += f'Host: {url_host}\r\n'
request += 'User-Agent: Python\r\n'
request += 'Connection: close\r\n\r\n'

# Iniciar conexão segura com o servidor
context         = ssl.create_default_context()
socket_rss      = socket.create_connection((url_host, RSS_PORT))
socket_rss_wrap = context.wrap_socket(socket_rss, server_hostname=url_host)
context.check_hostname = False  
context.verify_mode = ssl.CERT_NONE
# Enviar a requisição
socket_rss_wrap.send(request.encode(CODE_PAGE))
