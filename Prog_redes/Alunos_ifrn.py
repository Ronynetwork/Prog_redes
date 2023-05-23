import requests, sys

url = 'https://dados.ifrn.edu.br/dataset/d5adda48-f65b-4ef8-9996-1ee2c445e7c0/resource/00efe66e-3615-4d87-8706-f68d52d801d7/download/dados_extraidos_recursos_alunos-da-instituicao.json'

dados = requests.get(url).json() #Retirando do endereço url o arquivo que será utilizado
#print(dados[0])

# Questão 01: Listar os campus e a sua quantidade de alunos
campi = set(map(lambda x:x['campus'], dados)) #Utilizando das funções map e lambda para filtrar os campus dentro do arquivo dados
campi_alunos_aux = [] #Deixando o retorno dos campus no arquivo fora do loop para poder usar posteriormente
for x in campi:
    filtro = lambda c: c['campus'] == x #Criando uma variável de filtro para comparar os campus que forem iguais aos presentes na variável campi

    campi_alunos_aux.extend(filter(filtro, dados)) #Utilizando a formatação presente em filtro para extrair de dados a quantidade de vezes que o mesmo se repete
    campi_alunos = len(campi_alunos_aux) #Realizando a contagem final de repetições por campus
    print(f'Campi {x}: {campi_alunos} alunos matriculados.')
print('-'*100)
# Questão 02: Solicitar a sigla de um campus e listar os cursos do
#             campus e a quantidade de alunos de cada curso 
print('Iniciando a segunda parte da questão...')
print('-'*100)

try:
    sig_campus = str(input('Insira um campus para sua pesquisa:')).upper() #Utilizando a sintaxe de tentativa para evitar erros e deixar o output mais clean
    print('-'*100)
except:  
    print(f'Erro...{sys.exc_info()[0]}') #Utilizando do diretório sys para simplificar a mensagem e erro do sistema
    sys.exit
else:
    if sig_campus in campi:
        filtro1 = lambda cr: cr['campus'] == sig_campus #Criando um filtro para separar apenas o campus inserido no input
        campus_1 = tuple(filter(filtro1, campi_alunos_aux)) #criando uma tupla para armazenar o resultado da filtragem 
        cursos = set(map(lambda y:y['curso'],campus_1)) #Procurando dentro de campus_1 os cursos presentes no campus escolhido e utilizando set para evitar repetição
        for curso in cursos:
            filtro2 = lambda f: f['curso'] == curso #Criando um filtro para filtrar cada curso separadamente 
            alunos_curso_aux = tuple(filter(filtro2, campus_1)) #Armazenando em uma variável cada repetição do curso do filtro
            alunos_curso = len(alunos_curso_aux) #Fazendo a contagem de repetições
            print(f'Campi {curso}: {alunos_curso} alunos matriculados nesse curso.')
    else:
        print('Campus inexistente...')

print('-'*100)