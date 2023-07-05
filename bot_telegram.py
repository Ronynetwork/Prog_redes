import requests

API_KEY = '6338998807:AAGvV1OnJRlG24Bu5Au0n1N4HXnMg1KCWj8'

url_req = f'https://api.telegram.org/bot{API_KEY}'

requisicao = requests.get(url_req + '/getUpdates')

print(requisicao.status_code)

retorno = requisicao.json()

id_chat = retorno['result'][0]['message']['chat']['id']

mensagem = input('Digite algo')

resposta = {f'chat-id': id_chat, 'text':mensagem}

envio = requests.post(url_req + '/sendMessage', data=resposta)
print(envio)