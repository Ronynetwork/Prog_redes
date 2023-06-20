numero = int(input('Informe um Número Positivo: '))
numero = abs(numero)
aux = numero
soma = 0
cont = 1
tam = 0
while cont <= aux:
    cont *= 10
    tam += 1
while numero > 0:
    digito = numero%10
    potencia = digito**tam
    soma = potencia + soma
    numero = numero // 10
if soma == aux:
    print(f'O número {aux}, pertence aos Números de ARMSTRONG!')
else:
    print(f'O número {aux}, não pertence aos Números de ARMSTRONG!')