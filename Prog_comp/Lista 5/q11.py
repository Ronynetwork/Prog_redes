num1 = int(input('Informe o Primeiro número: '))
num2 = int(input('Informe o Segundo número: '))
if num1 > num2:
    maior = num1
    menor = num2 
else:
    maior = num2
    menor = num1
for cont in range(100):
    div = maior % menor
    if div == 0:
        break
    maior = menor
    menor = div
print(f'O Máximo Divisor Comum de {num1} e {num2} é {menor}\n')