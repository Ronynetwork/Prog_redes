import os, sys, socket, ssl
local = os.path.dirname(os.path.abspath(__file__)) 
print(local)
sys.path.append(local + '\\Funções')
import funções_link, funções_download

#url = input('informa a url: ')
link = input('Insira o endereço do arquivo que você deseja baixar:')

# Utilizando de função para modelar a url
link_quebrado, url_host, url_image, n_img, extensão, arq_txt, protocolo = funções_link.link_change(link)

print('-'*100)
print(arq_txt)
print(f'Host: {url_host}\nLocal_imagem: {url_image}')
print(f'Nome_imagem: {n_img}\nExtensão: {extensão}\nProtocolo: {protocolo}')
print('-'*100)

# Realizando a conexão
url_request, context, sockt_IPv4, sockt_img, buffer_size = funções_download.connect_skt()


print('Baixando o arquivo...')

# Pegando e armazenando o retorno dos dados
retorno = b''
while True:
    data = sockt_img.recv(buffer_size)
    if not data: 
        break
    retorno += data
#Fechando a conexão
sockt_img.close()

delimiter = '\r\n\r\n'.encode()
position  = retorno.find(delimiter) #Pegando a posição de início do cabeçalho
headers   = retorno[:position] # Armazenando o cabeçalho em Headers
image     = retorno[position+4:] # Pegando apenas a imagem

print('-'*100,'\n')
print(str(headers, 'utf-8'),'\n')
print('-'*100)

# Definindo o local do head
nome_cabeçalho = '\\arquivo' + arq_txt
local_cabeçalho = local + f'\\{nome_cabeçalho}'

# salvando o head em um arquivo
try:
    with open(local_cabeçalho, 'w', encoding='utf-8') as header:
        header.write(headers.decode('utf-8'))
except:
    print(f'Erro na criação do arquivo txt...{sys.exc_info()[0]}')

# Salvando a imagem
extensão_head = funções_link.extension_head # Recebendo a função criada
nome_final = f'{n_img}.' + extensão_head # Definindo o nome da imagem
imagem = local + f'\\{nome_final}' # Definindo o local de download

try:
    with open(imagem, 'wb') as arquivo:
        arquivo.write(image)
except:
    print(f'Erro ao salvar a imagem...{sys.exc_info()[0]}')
    exit()