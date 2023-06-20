import random
num = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 9
lista = list()
if num > 0:
    for i in range(num):
        lista.append(random.randint(inicio,fim))
    print(f'\nOs números foram: {lista}')
    print('\nA quantidade de repitação de cada número foi: ')
    for x in range(inicio, fim+1):
        print(f'{x} -> {lista.count(x)}')
    print('\nFIM!')
else:
    print('Informe um Número Positivo!')