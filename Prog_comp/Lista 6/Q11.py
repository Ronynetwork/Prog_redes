import random

letra = ['A', 'B', 'C', 'D','E']
certo = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E']
pessoas = ['Charles', 'Ronyldo', 'Bruno', 'Pedro', 'Kalvin', 'Cazuí', 'letícia', 'Ana', 'Carol', 'Amanda']
exames = list()

for nome in pessoas:
    exam = []
    exam.append(nome)
    for contador in range(10):
        numero = random.randint(0,4)
        exam.append(letra[numero])
    exames.append(exam)

for lista in exames:
    corretos = 0
    for contador in range(10):
        if certo[contador] == lista[contador + 1]:
            corretos += 1
    lista.append(corretos)

lista2 = []
for contador in range(11):
    for estudante in exames:
        if contador == estudante[-1]:
            lista2.insert(0, estudante)

print(150 * '=')
print(f'Gabarito: {certo}')
for estudante in lista2:
    print(f'O aluno(a) {estudante[0]} acertou {estudante[-1]}. Respostas: {estudante[1:11]}.')
print(150 * '=')