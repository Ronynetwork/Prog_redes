var = int(input('Informe um valor inteiro para realizar a sequência de Fibonacci: '))
aux1 = 1
resul = 0
valor2 = 0
aux2 = aux1
if var != 0:
    print(f'\nSua sequência para o valor [{var}] é:')
    for x in range(aux1,var+1):
        resul = aux2 + valor2
        print(resul, end='-')
        aux1 +=1
        aux2 = valor2
        valor2 = resul
    print(''); print('\nEsses são os valores da sua sequência!\n')
else: print('\nO valor informado é igual a zero. Informe outro.\n')