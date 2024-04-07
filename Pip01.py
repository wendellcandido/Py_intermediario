## PIP 
 import requests

 cep = input('Qual seu CEP?')

 url = f'https://viacep.com.br/ws/{cep}/json'

 resposta = requests.get(url)
 print(resposta.text)