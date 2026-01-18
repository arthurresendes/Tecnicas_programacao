import calendar

calendar.prcal(2025)
print("-"*80)
print(calendar.calendar(2026))
print("-"*80)
print(calendar.month(2025, 12))
print("-"*80)
calendar.prmonth(2026,1)
print("-"*80)
dia_semana  = calendar.weekday(2025, 12, 12)
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
print("-"*80)
print(calendar.weekheader(6))
print("-"*80)
print(calendar.isleap(2020)) # Verifica se é bissexto
print("-"*80)
print(calendar.leapdays(2010, 2025)) # Retorna quantidade de anos bissextos de 2010 ate 2024

print("-"*80)
c = calendar.Calendar(calendar.SUNDAY)
for weekday in c.iterweekdays():
    print(weekday, end=" ")

print(end="\n")
print("-"*80)
c = calendar.Calendar()
for date in c.itermonthdates(2019, 11):
    print(date, end=" ")


print(end="\n")
print("-"*80)
c = calendar.Calendar()
for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")


print(end="\n")
print("-"*80)
c = calendar.Calendar()
for data in c.monthdays2calendar(2025, 12):
    print(data) # (Dia,Dia em numero de 0 até 6, sendo 0 seg e 6 dom)
