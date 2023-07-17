import os, sys
#                                          VARIÁVEIS                                                   <:

SERVER = '0.0.0.0'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '
CLIENT = 'localhost'
CODE = 'utf-8'




dir_atual = os.path.dirname(os.path.abspath(__file__)) # pegando sua pasta atual dir_past = dir_atual + '\\Functions and Variables'
dir_past = dir_atual + '\\Functions and Var'
name_arqs = ['functions_bot.py', 'functions_client.py', 'functions_others.py', 'functions_server.py', 'variables.py']
functions_arq = os.listdir(dir_past)
'''
 VERIFICAÇÃO SE TODOS OS ARQUIVOS/PASTAS DE FUNÇÕES ESTÃO PRESENTES '''

try:
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\Functions and Variables') # adicionando a pasta de funções na config de pesquisa de funções do sistema functions_arqos.listdir (dir_past) 
    # listando arquivos da pasta onde está as funções para verificar se todos os arquivos necessários estão
    for arquivos in name_arqs:
    if arquivos not in functions_arq: #vendo qual o arquivo que falta
        print("\no Arquivo "[arquivos)" não está presente dentro da pasta "Functions and Variables"," +'faça o download dele para o funcionamento correto do código!\n")
        exit()
 except FileNotFoundError: # para casa a pasta não exista
print("\nA pasta "Functions and Variables" não foi encontrada, faça o download dela para o
 + "funcionamento correto do código [com todas suas dependencias]!\n')

sys.exit()
 except:
print("\nErro na Verificação dos arquivos da Pasta de Funções...(sys.exc_info()[0]}")