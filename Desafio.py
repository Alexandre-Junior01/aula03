'''problema:
Dados os valores de horários abaixo, decifre a lógica e faça um código para executar.'''

h1 = int(input("digite a hora1: "))
m1 = int(input("digite a min1: "))
h2 = int(input("digite a hora2: "))
m2 = int(input("digite a min2: "))

if h1 > 12:
   h1= h1-12

if h2 > 12:
  h2 = h2 - 12
somaH= h1+ h2
if somaH >24:
   somaH = somaH -24
elif somaH >12:
    somaH= somaH -12
print(somaH)
somaM= m1+ m2
if somaM>59:
    somaH = somaH+1
    somaM= somaM -60
print(somaH,somaM)




