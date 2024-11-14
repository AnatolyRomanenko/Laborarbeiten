import math
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))
if math.atan(x) - math.atan(z) == 0:
    print('На ноль дельть нельзя')
else:
    a1 = math.atan(x) - math.atan(z)
    d = math.log(y, math.e)
    d1 = d * d
    a2 = math.pow(d1, 1 / 3)
    h = math.fabs(x - y)
    a3 = math.pow(math.e, h)
    h1 = x + y
    a4 = math.pow(h, h1)
    s = ((a3 + a4) / a1) + a2
    print("s= ", s)