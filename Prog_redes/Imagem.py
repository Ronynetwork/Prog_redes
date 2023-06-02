import os, sys
local = os.path.dirname(os.path.abspath(__file__)) 
sys.path.append(local+'//Funções')
import funções_link 

print(local)
'''#url = input('informa a url: ')
link = input('Insira o endereço do arquivo que você deseja baixar:')

# Utilizando de função para modelar a url
url_host, n_img, link_quebrado, extensão, url_image = funções_link.link_change(link)

print('-'*100)
print(f'\nhost:{url_host}\nlocal_imagem:{url_image}')
print(f'\nnome_imagem:{n_img}\nextensão:{extensão}\nprotocolo:{protocolo}\n')
print('-'*100)

# Define a porta se a url for HTTP ou HTTPS
if protocolo == 'https':
    try:
        buffer_size = 1024 
        porta = 443
        url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_img = context.wrap_socket(sockt, server_hostname=url_host)
        sock_img.connect((url_host, porta))
        sock_img.send(url_request.encode())
        print('Baixando a imagem...')
    # Montado a variável que armazenará os dados de retorno
        retorno = b''
        while True:
            data = sock_img.recv(buffer_size)
            if not data: 
                break
            retorno += data
        sock_img.close()
        
        # Separando o Cabeçalho dos Dados
        delimiter = '\r\n\r\n'.encode()
        position  = retorno.find(delimiter)
        headers   = retorno[:position]
        image     = retorno[position+4:]

        print('-'*100,'\n')
        print(str(headers, 'utf-8'),'\n')
        print('-'*100)
    except :
        print(f'Erro...{sys.exc_info(0)}')  
        exit()      

elif protocolo =='http':
    try:
        #Identificando a porta e gerando o get
        url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
        porta   = 80
        buffer_size = 1024
        #Estabelecendo a conexão
        sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_img.connect((url_host, porta))
        sock_img.send(url_request.encode())

        print('Baixando a imagem...')

        # Pegando e armazenando o retorno dos dados
        retorno = b''
        while True:
            data = sock_img.recv(buffer_size)
            if not data: 
                break
            retorno += data
        #Fechando a conexão
        sock_img.close()
        delimiter = '\r\n\r\n'.encode()
        position  = retorno.find(delimiter)
        headers   = retorno[:position]
        image     = retorno[position+4:]

        print('-'*100,'\n')
        print(str(headers, 'utf-8'),'\n')
        print('-'*100)

    except :
        print(f'Erro...{sys.exc_info(0)}')  
        exit()      
else:
    print(f'O protocolo inserido não é suportado... \nTente novamente utilizando HTTP ou HTTPS.')

# Tratamento de caracteres especiais no nome do head
special = [';','.','*','?','/','>','<','|','"']
contem = 0
for letra in special:
    while contem != -1:
        contem = n_img.find(letra)
        n_img = n_img.replace(letra,'-')

# Definindo o local do head
dir_cabeçalho = local + f'\\{n_txt}'

# salvando o head em um arquivo
try:
    with open(n_img, 'w', encoding='utf-8') as header:
        header.write(headers.decode('utf-8'))
except:
    print(f'Erro...{sys.exc_info()[0]}')
    exit()

#identificando o locando onde é localizado as extensões no head
chave_extensão = 'Content-Type'

# Localizando o arquivo cabeçalho
dir_cabeçalho = local + f'\\{n_img}'

# Realizando a tentativa de encontrar a extensão
try:
    with open(dir_cabeçalho, 'r', encoding='utf-8') as leitor_cabeçalho:
        for x in leitor_cabeçalho:
            if chave_extensão in x:
                extensão_head = x.split('/')[1].strip()
except:
    print(f'Erro...{sys.exc_info()[0]}')
    exit()

# Salvando a imagem com a nova extensão
nome_final = 'imagem.' + extensão_head
imagem = local + f'\\{n_img}'

try:
    with open(imagem, 'wb') as img:
        img.write(image)
except:
    print(f'Erro...{sys.exc_info()[0]}')
    exit()
'''