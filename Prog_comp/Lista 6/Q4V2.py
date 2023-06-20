import random
num = int(input('\nInforme quantos números você quer: '))
inicio = 0
fim = 99
lista = list()
if num > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(num) ]
    print(f'A lista original é:\n{lista}')
    print('-'*150)
    lista.sort(reverse=True)
    print(f'A lista alterada é:\n{lista}')
else:
    print('Informe um Número Positivo!')