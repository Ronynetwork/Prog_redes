mi = float(input("determine o peso inicial em gramas: "))
mf = mi
aux = 0
tmph = 0
tmpm = 0
tmps = 0
while mf >= 0.5:
    mf = mf/2
    aux +=1
tmph = (aux * 50)/3600
tmpm = (aux * 50)/60
tmps = aux*50
print('');print(f"Massa inicial: {mi}g. Massa final: {mf:.2f}g. Tempo em horas: {tmph:.3f}h. Tempo em Minutos: {tmpm:.3f}min. Tempo em Segundos {tmps}s\n")