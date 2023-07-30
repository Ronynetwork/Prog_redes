num = int(input('Insira o valor do número que deseja verificar:'))
divisor = 3
if num < 3:
    print('Esse número não pode ser dividido normalmente por 3.')
else:
    print('O número pode ser dividido por 3:\nRealizando a divisão...\n')
    resultado = float(num/divisor)
    print(f'A divisão de {num} por 3 gerou esse resultado: {resultado}.')