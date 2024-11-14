import math
x1 = float(input("Введите значение x1 -> "))
xn = float(input("Введите значение xn -> "))
delx = float(input("Введите значение delx -> "))
a = float(input("Введите значение a -> "))
y = 0
while x1 < xn:
    y += a * x1 * (1 + a * math.pow(math.e, -x1))
    x1 += delx
print("y=: ", y)