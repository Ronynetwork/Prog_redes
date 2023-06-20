import random
num = int(input('\nInforme quantos numerais você quer que repita: '))
inicio = 0
fim = 99
lista = list()
if num > 0:
    for x in range(num):
        lista.append(random.randint(inicio,fim))
    print(f'\nOs números foram: {lista}\n')
    print('='*150)
    soma1 = 0
    soma2 = 0
    soma3 = 0
    soma4 = 0
    for y in range(inicio, fim+1):
        cont = lista.count(y)
        if y < 25:
            soma1 += cont
        elif y >= 25 and y <= 49:
            soma2 += cont
        elif y >= 50 and y <= 74:
            soma3 += cont
        elif y >= 75 and y <= 99:
            soma4 += cont
    print(f'\nOs números do 1° QUARTIL Repetiram -> {soma1}x')
    print(f'\nOs números do 2° QUARTIL Repetiram -> {soma2}x')
    print(f'\nOs números do 3° QUARTIL Repetiram -> {soma3}x')
    print(f'\nOs números do 4° QUARTIL Repetiram -> {soma4}x')
    print('\nFIM!\n')
else:
    print('Informe um Número Positivo!')