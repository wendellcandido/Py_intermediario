## ADICIONAR VALIDAÇÃO SE A PESSOA DIGITOU NUMERO OU OUTRO CARACTER COLOCCAR VALIDAÇÃO

 import requests
 import re

 cep = input('Qual seu CEP?')
 cep = re.sub('[^0-9]', '', cep)

 url = f'https://viacep.com.br/ws/{cep}/json'

 resposta = requests.get(url)
 print(resposta.text)