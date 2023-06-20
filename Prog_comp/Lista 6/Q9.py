import random
num = int(input('\nInforme quantos numerais você quer: '))
inicio = 0
fim = 1000
lista = list()
if num > 0:
    for i in range(num):
        lista.append(random.randint(inicio,fim))
    print(lista)
    valor = int(input('Insira o valor que deseja pesquisar na lista entre 0-1000:'))
    if valor not in lista: 
        print(f'\n{valor} não se encontra na lista!\n')
    else:
        print(f'\n{valor} se encontra na lista na {lista.index(valor)}º posição.\n')
else: 
    print('Informe um Número Positivo!')