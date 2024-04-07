## GERAR QRCODE WHTASAPP
 import qrcode

 tel = input('Meu telefone')
 url = f'api.whatsapp.com/send/?phone={tel}'
 cel = qrcode.make(url)
 cel.save('whatsapp.jpg')