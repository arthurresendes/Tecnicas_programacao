from mod import fun

fun()

import math
print(dir(math))

# file a.py
print("a", end='')


print(__name__)



try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c")


x = "\\\\"
print(len(x))

print(chr(ord('p') + 2))

print(float("1.3"))




class A:
    def a(self):
        print('a')


class B:
    def a(self):
        print('b')


class C(B, A):
    def c(self):
        self.a()


o = C()
o.c()

try:
    raise Exception(1, 2, 3)
except Exception as e:
     print(len(e.args))


def my_fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in my_fun(2):
    print(x, end='')

class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v


for x in I():
    print(x, end='')

def o(p):
    def q():
        return '*' * p
    return q


r = o(1)
s = o(2)
print(r() + s())



numbers = [0, 2, 7, 9, 10]
foo = list(map(lambda x: x ** 2,numbers))
print(list(foo))

numbers2 = [i*i for i in range(5)]
foo2 = list(filter(lambda x: x %2,numbers2))
print(foo2)

from datetime import datetime

datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)

print(datetime_1 - datetime_2)

from datetime import timedelta

delta = timedelta(weeks = 1, days = 7, hours = 11)
print(delta * 2)

import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))

