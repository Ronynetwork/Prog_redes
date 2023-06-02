
# Código para realizar commit e push automatico no GITHUB

import subprocess, time, os, platform

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('='*100)
ascii_art = r"""
   _____ _ _   _           _                     _                        _   _             
  / ____(_) | | |         | |         /\        | |                      | | (_)            
 | |  __ _| |_| |__  _   _| |__      /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __  
 | | |_ | | __| '_ \| | | | '_ \    / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 | |__| | | |_| | | | |_| | |_) |  / ____ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
  \_____|_|\__|_| |_|\__,_|_.__/  /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                                                                            
                                     by - kakanetwork
 """                                                                                                                       
print(ascii_art)

print('='*100)

def Git_Push ():
    print('='*100)
    modo = ''
    while modo not in ['A', 'U', 'S', '?']:
        modo = str(input('\nModos:\nA - Automatico\nU - Único\nS - Sair\n? - Ajuda\n\nQual você deseja? ').upper())
        if modo not in ['A', 'U', 'S', '?']:
            print('Tente Novamente... informe corretamente!')
    
    commit_name = 'Atualizado'
    branch_origin = 'home'
    tempo_seg = 120
    print('')
    print('='*100)
    if modo == 'A':
        while True:
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', commit_name])
            subprocess.call(["git", "push", "-u", "origin", branch_origin])
            print('='*100)
            time.sleep(tempo_seg) 

    elif modo == 'U':
        print('')
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', commit_name])
        subprocess.call(["git", "push", "-u", "origin", branch_origin])
        print('\nVolte sempre!\nby kakanetwork')
        print('\n'+'='*100)

    elif modo == '?':
        print(f'\nExplicação das Variavéis:\n\nAutomático -> Será gerado um Commit a cada {tempo_seg}s até que você encerre o programa! (se desejar alterar os segundos, acesse a configuração)\n\
Único -> Será gerado um Commit Único e o Programa será encerrado!\n\nCommit_name -> O nome do seu commit, pode ser genérico (se necessário alteração, vá nas configurações)!\n\
Branch_Origin -> O nome do seu branch default no Github (se necessário alteração, vá nas configurações)!\n')
        print('='*100)
    elif modo == 'S':
        print('\nPrograma Encerrado com Sucesso! :(\n')
        exit()

def Git_Pull ():
    print('='*100)
    print('')
    subprocess.run(['git', 'pull'])
    print('\nVolte sempre!\nby kakanetwork')
    print('\n'+'='*100)

def Git_Connect ():
    print('='*100)
    print('\nem desenvolvimento...')

def Ajuda ():
    print('='*100)
    print(f'\nGit Push -> Realiza o Push do seus Commits, ou seja leva a atualização deles para o seu github\nGit Pull -> Realiza o Pull dos seus commits, \
ou seja traz as atualizações do seu código no github para seu ambiente de programação\nGit Connect -> Vai realizar a conexão do seu github com o seu VSCODE \
automaticamente (Recomendado realizar antes de qualquer Pull ou Push.)!\n')
    print('='*100)

def Sair ():
    print('='*100)
    print('\nPrograma Encerrado com Sucesso! :(')
    exit()

opções = {
    '1': Git_Push,
    '2': Git_Pull,
    '3': Git_Connect,
    '4': Ajuda,
    '5': Sair
}   

opções_descritivas = {
    '1': 'Realizar Push no GitHub',
    '2': 'Realizar Pull do GitHub',
    '3': 'Conectar ao GitHub',
    '4': 'Exibir Ajuda',
    '5': 'Sair do Programa'
}

print('\nFerramentas Disponiveis:\n')

for key, value in opções_descritivas.items():
    print(f'{key}: {value}')

ferramenta = ''

while ferramenta not in opções:
    ferramenta = input('\nQual Ferramenta deseja utilizar? ')
    if ferramenta not in opções:
        print('Tente Novamente... informe corretamente!')

print(f'Você escolhou a ferramenta: {opções_descritivas[ferramenta]}\n')
opções[ferramenta]()
