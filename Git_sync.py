# Código para realizar commit e push automatico no GITHUB

import subprocess
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Atualizado'])
subprocess.call(["git", "push", "-u", "origin", "home"])