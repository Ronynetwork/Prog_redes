'''commands = {
    'oi':'iai',
    'olá': 'fala',
    'escuta':'to ouvindo'
}

comando = input('Insira seu comando:')

funcao_associada = commands[comando]
funcao_associada()'''


import sys, os
def List_Server():
    try:
        local =  os.path.dirname(os.path.abspath(__file__)) + '\\server_files\\'
        # Obtém a lista de itens (arquivos e diretórios) no diretório especificado
        itens_no_diretorio = os.listdir(local)
        print('-'*100);print(f'Estes são os arquivos presentes na pasta do servidor e seus respectivos tamanhos:\n')
        # Filtra apenas os arquivos
        for item in itens_no_diretorio:
            lenght = os.path.getsize(local+item)
            print(f'({item}): {lenght} bytes;')
        print('-'*100)
        print('Caso deseje realizar o download de algum arquivo, por favor utilizar o comando (/d:(nome do arquivo)).')
    except FileNotFoundError:
        print("Diretório não encontrado.")

List_Server()