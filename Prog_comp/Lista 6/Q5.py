import random
numerais = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 99
lista = list()
if numerais > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(numerais)]
    lista.sort()
    print(f'\nOs números foram: {lista}\n')
    num2=0
    for x in lista:
        num2+=x
    media = num2/numerais
    print(f'A média é: {media:.2f}')
    posmeio = int(numerais/2)
    if numerais%2 == 0:
        mediana = (lista[posmeio] + lista[posmeio-1])/2
        print(f'A mediana é: {mediana}')
    else:
        print(f'A mediana é: {lista[posmeio]}')
    varia_pop = 0
    desvio = 0
    for y in lista:
        varia_pop += (x-media)**2
    varia = varia_pop/(numerais-1)
    desvio = varia**(1/2)
    print(f'A Variância Populacional é: {varia:.2f}')
    print(f'O Desvio é: {desvio:.2f}')