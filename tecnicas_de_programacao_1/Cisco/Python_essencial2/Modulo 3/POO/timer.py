class Timer:
    def __init__(self, horas,minutos,segundos):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return f"{self.__horas}:{self.__minutos}:{self.__segundos}"

    def next_second(self):
        self.__segundos += 1
        if self.__segundos == 60:
            self.__segundos = 00
            
            self.__minutos += 1
            if self.__minutos == 60:
                self.__minutos = 00
                self.__horas += 1
                if self.__horas == 24:
                    self.__horas = 00



    def prev_second(self):
        if self.__segundos == 00:
            self.__segundos = 59
            if self.__minutos == 00:
                self.__minutos = 59
                if self.__horas == 00:
                    self.__horas = 23
        else:
            self.__segundos -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

timer2 = Timer(12, 23, 42)
print(timer2)
timer2.prev_second()
print(timer2)
timer2.prev_second()
print(timer2)
timer2.next_second()
print(timer2)
