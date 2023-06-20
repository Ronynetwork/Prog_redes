import random
num = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 9
lista = list()
if num > 0:
    list2 = [lista.append(random.randint(inicio,fim)) for i in range(num)]
    print(f'\nOs números foram: {lista}\n')
    print('\nA quantidade de repitação de cada número foi: ')
    list3 = [print(f'{i} -> {lista.count(i)}') for i in range(inicio,fim+1) ]
    print('\nFIM!')
else: 
    print('Informe um número Positivo!')