#funcionalidades de strings
frase = 'Quero comer pipoca'

#Fatiamento (Pega a posição por meio de [])
frase[9]
'''Pega o valor de string referente a posião indicada, lembrando que a posição é contada a partir do 0 e o último caractere é desconsiderado'''
#Fatiamento composto
frase[1:5]
'''Os : servem para separar início e fim da quebra da string, se não houverem valores em algum dos lados ele irá do início(esquerda) ou até o final(direita)'''
#Saltos dentro de uma string
frase[1:4:2]
'''O  ultimo valor numérico separa a string pulando a quantidade informada de posições'''
#Contabilizando caracteres:
len(frase)
'''Contabiliza a quantidade de caracteres de uma string'''
# Contabilizando repetições de caracteres
frase.count('o')
'''Contabiliza quantas strings iguais a informada existem na variável em questão, é possível realizar o fatiamento da string dentro do count
separando a string por vírgula envez de ":".'''
# Localiza o início da string em questão
frase.find('o')
'''Indica onde se localiza o início da string procurada '''
# Indicar se existe ou não
'Quero' in frase
'''Indica se o valor está(True) ou não está (false) na frase'''
# Intuitivo, substitui umas string por outra
frase.replace('Quero', 'Não quero')
'''Substitui a string exata da esquerda pela da direita'''
# Caixa alta e caixa baixa respectivamente:
frase.lower(), frase.upper()
'''Deixam a string inteira em minúsculo e maiúsculo respectivamente'''
# Maiúsculo:
frase.capitalize()
'''Coloca apenas a primeira posição da string em maiúsculo'''
frase.title()
'''Coloca todas as primeiras letras após um espaço vazio em maiúsculo'''
#Remover espaços 
frase.strip()
'''Remove todos os espaços antes da primeira e depois da última string, colocando "l" ou "r"' antes de strip você indica de qual lado deseja remover os espaços'''
