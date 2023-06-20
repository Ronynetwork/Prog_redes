a = int(input('Insira um número inteiro positivo:'))
binario = ''
for x in range(a+1):
    if a > 0:
        resto = a%2
        a = a//2
        binario = str(resto)+binario
print(f'\n O valor em binário do número inserido é [{binario}] \n')