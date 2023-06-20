val = int(input('Informe o primeiro valor da P.A: '))
raz = int(input('Informe a Razão da P.A: '))
qnt_val = int(input('Quantos termos vc deseja encontrar: '))
pos = int(input(f'Informe a Posição do valor que você quer saber\n(A posição deve ser menor ou igual a {qnt_val}): '))
qnt_val = abs(qnt_val)
prim=val
soma=0
cont=1
numpos=0
while cont <= qnt_val:
     print(prim, end=' , ')
     soma = prim + soma
     prim+=raz
     cont+=1
     if cont == pos and pos <= qnt_val:
         numpos = prim
print('FIM DA P.A!')       
print(f'\nA soma da P.A é igual á {soma}!')
print(f'O número referente a {pos}° Posição na P.A, é o {numpos}!')
if raz > 0:
     print('E Sua P.A é crescente!')
elif raz < 0:
     print('E Sua P.A é Descrescente!')
else:
     print('E Sua P.A é constante!')