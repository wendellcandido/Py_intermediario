## CRIAR PESSOA FAKE
 from faker import Faker

 fake = Faker()
 nome_completo = fake.name()
 print('Seu Cuca ill')
 email = fake.email()
 print(email)