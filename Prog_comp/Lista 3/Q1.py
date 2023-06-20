a = int(input('Insira um número inteiro positivo:'))
a = abs(a)
binario = ''
while a > 0:
    resto = a%2
    a = a//2
    binario = str(resto)+binario
print(f'\n O valor em binário do número inserido é {binario} \n')