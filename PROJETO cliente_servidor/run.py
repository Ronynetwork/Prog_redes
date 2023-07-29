import platform, os, sys, subprocess, signal

dir_atual = os.path.dirname(os.path.abspath(__file__)) 
dir_arq =  os.path.abspath(__file__) 
dir_pid = dir_atual + "\\pid.conf" # montando pasta
system = platform.system().lower() # pegando nome do sistema

def KILL_PROCESS(PID):
    try:
        os.kill(int(PID), signal.SIGTERM) # uso o os.kill pela praticidade 
        os.remove(dir_pid) # removo o arquivo do pid
        print('\nO Server foi Desligado com sucesso!\n')
    except:
        os.remove(dir_pid) # para caso exista um pid, mas não seja válido, apago o arquivo também
        print('\nO Server ainda não foi Iniciado!\n')


def RUNNER():
    try:
        if system == 'windows': # verificação de sistema 
            # utilizo o subprocess para executar ele em 2° plano e retornar o seu PID original
            process = subprocess.Popen["pythonw", "app_server.py"].pid
        elif system == 'linux':
            process = subprocess.Popen["python", "app_server.py", "&"].pid
        with open(dir_pid, "w") as file:
            file.write(str(process)) # após inicializar escrevo no arqivo do pid o número do pid 
        print(f'\nO Servidor foi iniciado em 2° Plano com sucesso!\nPID -> {process}\n')
    except:
        print(f'\nErro na hora de Rodar o Processo! {sys.exc_info()[0]}')
        sys.exit()



def PID_VERIFICATION(PID):
    try:
        if system == 'windows': # verificação de sistema
            # com o RUN ele me retorna detalhes do processos, logo se for False/None, o processo não existe
            processo = subprocess.run(['Powershell', 'Get-Process', '-Id', PID], capture_output=True, text=True).stdout.strip()
        elif system == 'linux':
            processo = subprocess.run(['ps', '-p', PID], capture_output=True, text=True).stdout.strip()
    except: 
        print(f'\nErro na hora de Verificar o PID! {sys.exc_info()[0]}')
    else:
        if processo:
            print(f'\nO Server já está sendo rodado em 2° Plano com o PID: {PID}\n')
            sys.exit()
        else:
            RUNNER()
