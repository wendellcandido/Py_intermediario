
## EXTREMAMENTE BASICO 1001
A = (int(input('')))
B = (int(input('')))
X = A + B

print(f'X = {X}') 

## AREA DO CIRCULO 1002
raio = float(input())
pi = 3.14159
area = pi * raio * raio 
print(f'A={area:.4f}')

## SOMA SIMPLES 1003
A = int(input(''))
B = int(input(''))
soma = A + B
print("SOMA =", soma)

## TESTE DE SELEÇÃO 1 1035
linha = input()
lista = linha.split()

a = int(lista[0])
b = int(lista[1])
c = int(lista[2])
d = int(lista[3])

if b > c and d > a and c + d > a + b and c >=0 and d >=0 and a %2  ==0:
    
    print('Valores aceitos')
    
else:
    print('Valores nao aceitos')


## LANCHE 1038
cod, quant = input().split()
cod = int (cod)
quant = int(quant)
if (cod == 1):
    total = quant * 4
elif (cod == 2):
    total = quant * 4.5
elif (cod == 3):
    total = quant * 5
elif (cod == 4):
    total = quant * 2
elif (cod == 5):
    total = quant * 1.5
print("Total: R$ %.2f" %total)


## TRIANGULO 1043
a, b, c = map(float, input().split())
perimetro = a+b+c
area = (a+b) * c/2
if (a<(b+c)) and (b<(a+c)) and (c<(a+b)):
    print('Perimetro = %.1f'%perimetro)
else:
    print('Area = %.1f' %area)


## NUMEROS POSITIVOS
cont_positivos = 0
for i in range(6):
    valor = float(input())
    if valor > 0:
        cont_positivos += 1

print(f'{cont_positivos} valores positivos')


## seis numeros impares 1070
x = int(input())
for i in range(x, x+12):
    if(i%2!=0):
        print(i)













