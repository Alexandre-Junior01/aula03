time1= input('Digite nome do time: ')
time2 =input('Digite nome do time: ')
golsTime1 = int(input('digite golstime1: '))
golsTime2= int(input('digite golstime2: '))
if golsTime1 > golsTime2:
    print(f"time {time1} ganhou {golsTime1}")
elif golsTime2>golsTime1:
    print(f" time {time2} ganhou {golsTime2}")
else:
    print("empate")
