valor = int(input('Informe um valor parar iniciar a P.A: '))
razao = float(input('Agora informe a razão da P.A: '))
qntt = int(input('Quantos termos quer encontrar na P.A? '))
posi = int(input(f'Agora informe a posição do valor que deseja verificar\n(Lembrando que o valor deve ser menor ou igual a {qntt}): '))
qntt = abs(qntt)
p_a=valor
soma=0
cont=1
np=0
for x in range(cont,qntt+1):
     print(p_a, end=' , ')
     soma = p_a + soma
     p_a+=razao
     cont+=1
     if cont == posi and posi <= qntt:
         np = p_a
print('P.A encerrada!')       
print(f'A soma da P.A é igual á {soma}!')
print(f'O número correspondente a {posi}° posição na P.A é = {np}!')
if razao > 0: print('P.A crescente!')
elif razao < 0: print('P.A descrescente!')