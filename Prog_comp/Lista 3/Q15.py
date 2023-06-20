num = int(input("Digite o valor de N inteiro e positivo: "))
aux = 1
if num > 0:
    while aux * (aux+1) * (aux+2) <= num:
        aux = aux + 1
    if aux * (aux+1) * (aux+2) == num: print(f"o numero {num} é triangular")
    else: print(f"o numero {num} não é triangular")
else: print('Insira um valor inteiro e positivo')