num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
maior, menor = num1, num2
nums,contador = '', 2
for contador in range(100):
    if maior == 1 or menor == 1: break
    if maior % contador == 0 and menor % contador == 0:
        nums += str(contador)
        maior //= contador
        menor //= contador
    else:
        if maior % contador == 0 or menor % contador == 0:
            if maior % contador == 0: maior //= contador
            elif menor % contador == 0: menor //= contador
        else: contador +=1
multiplicação = 1
for num in nums : multiplicação *= int(num)
print(f'O maior divisor comum de {num1} e {num2} é {multiplicação}.')