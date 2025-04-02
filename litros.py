
combust= input('digite E para etanol ou G para gasolina:').upper()
etanol = 4.90
gasolina = 5.80
if combust=="E":

    litros=float(input('digite a quantidade de litros: '))
    print(f'litros gasto {litros*etanol:.2f}')
elif combust=="G":

    litros = float(input('digite a quantidade de litros: '))
    print(f'litros gasto {litros*gasolina:.2f}')
else:
    print('Digite e ou g')