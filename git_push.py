
# Código para realizar commit e push automatico no GITHUB

import subprocess, time, os, platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('='*100)
print('\nFUNCIONAMENTO DO CÓDIGO:\nNo modo automático o commit será realizado a cada 1min até você parar a execução... no modo único ele será realizado apenas uma vez...\n')
print('='*100)

modo = ''
while modo != 'A' and modo != 'U':
    modo = input('\nEscolha o Modo: Automático(A) Único(U) ou Sair(S): ').upper()
    if modo == 'S':

        print('\n'+'='*100)
        print('\nCódigo encerrado com sucesso!\n')
        break

commit_name = 'Atualizado'
branch_origin = 'master'
tempo_seg = 120

if modo == 'A':
    while True:
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', commit_name])
        subprocess.call(["git", "push", "-u", "origin", branch_origin])
        print('='*100)
        time.sleep(tempo_seg) 

elif modo == 'U':
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', commit_name])
    subprocess.call(["git", "push", "-u", "origin", branch_origin])
    print('\n'+'='*100)