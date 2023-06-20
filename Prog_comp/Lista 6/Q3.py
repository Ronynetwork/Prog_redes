import random
num = int(input('\nInforme quantos numerais você quer: '))
inicio = 0
fim = 99
lista = list()
if num > 0:
    for a in range(num):
        lista.append(random.randint(inicio,fim))
    print(f'A lista original é:\n{lista}')
    print('='*100)
    lista_ord = list()
    tam = len(lista)
    for x in range(tam):
        menor = lista[0]
        for y in range(len(lista)):
            if lista[y] < menor:
                menor = lista[y]
                pos_menor = y
        lista_ord.append(menor)
        lista.remove(menor)
    print(lista_ord)
else:
    print('Informe um Número Positivo!')