from datetime import date,time,datetime,timedelta

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


meu_aniversario = date(2006, 12, 1)
print(meu_aniversario)

import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)


d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)


dia_semana = today.weekday()
if dia_semana == 0:
    print("Segunda")
elif dia_semana == 1:
    print("Terça")
elif dia_semana == 2:
    print("Quarta")
elif dia_semana == 3:
    print("Quarta")
elif dia_semana == 4:
    print("Sexta")
elif dia_semana == 5:
    print("Sabado")
else:
    print("Domingo")


print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


delta = timedelta(weeks=2, days=2, hours=3)
print(delta)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)