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
        system = platform.system().lower()  # Verficando o tipo de sistema operacional

        if system == 'windows':
            #Utilizando subprocess para rodar o script em segundoi plano e encontrar eu PID 
            process = subprocess.Popen(["pythonw", "servidor.py"]).pid
        elif system == 'linux':
            process = subprocess.Popen(["python", "servidor.py", "&"]).pid

        dir_pid = "pid.txt"  # Assume que o nome do arquivo é 'pid.txt'
        with open(dir_pid, "a") as file:
            file.write(str(process) + "\n")  # Adiciona o PID nos processos

        print(f'\nO servidor está em background com sucesso!!\nPID -> {process}\n')
    except Exception as e:
        print(f'\nErro enquanto tentava rodar o processo... {e}')
        sys.exit()




def PID_VERIFICATION(PID):
    try:
        if system == 'linux':
            processo = subprocess.run(['ps', '-p', PID], capture_output=True, text=True).stdout.strip()
        elif system == 'windows': # verificação de sistema
            # com o RUN ele me retorna detalhes do processos, logo se for False/None, o processo não existe
            processo = subprocess.run(['Powershell', 'Get-Process', '-Id', PID], capture_output=True, text=True).stdout.strip()
    except: 
        print(f'\nErro ao Verificar o PID! {sys.exc_info()[0]}')
    else:
        if processo:
            print(f'\nO Server já está em 2° Plano com o PID: {PID}\n')
            sys.exit()
        else:
            RUNNER()
