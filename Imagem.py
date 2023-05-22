import socket

# Solicitando o link da imagem a ser baixada:
link = input('Insira o link da imagem em que deseja realizar o download:')

# Separando em formato de lista com o método split:
link_separado = link.split('/')

# Utilizando a posição dos separadores para extrair o host:
conexão = link_separado[0]
print(conexão)
url_host=link_separado[2]
# apagando os valores menores que url_host:
del link_separado[:3]

# Unindo os elementos filtrados novamente em uma string:
url_image = '/' + '/'.join(link_separado)

# Realizando a troca de extensão
extensão = link.split('.')[-1]
link_txt = link.replace(extensão,'txt')
print(link_txt)
print('-'*100);print(f'Seu host é ({url_host}).\nSua imagem é ({url_image}).');print('-'*100)

# definindo o tipo de conexão:
if conexão == 'http:':
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
    host_port   = 80
    buffer_size = 1024

elif conexão == 'https:':
    url_request = f'GET {url_image} HTTPS/1.1\r\nHOST: {url_host}\r\n\r\n' 
    host_port   = 443
    buffer_size = 1024
# Buscando url da imagem:
sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, host_port))
sock_img.sendall(url_request.encode())

print('\nBaixando a imagem...')
# Montado a variável que armazenará os dados de retorno
data_ret = b''
while True:
    data = sock_img.recv(buffer_size)
    if not data: break
    data_ret += data

sock_img.close()

# Obtendo o tamanho da imagem
img_size = -1
tmp = data_ret.split('\r\n'.encode())
for line in tmp:
   if 'Content-Length:'.encode() in line:
      img_size = int(line.split()[1])
      break
print(f'\nTamanho da Imagem: {img_size} bytes')

# Separando o Cabeçalho dos Dados
delimiter = '\r\n\r\n'.encode()
position  = data_ret.find(delimiter)
headers   = data_ret[:position]
image     = data_ret[position+4:]

# Salvando a imagem
file_output = open('image.txt', 'wb')
file_output.write(image)
file_output.close()
