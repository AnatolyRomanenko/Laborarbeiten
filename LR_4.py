str = input("Введите строку -> ")
str1 = ""
n = 0 #кол-во замен
for c in str:
    if c == "%" :
        c = ":"
        n = n + 1
    str1 = str1 + c
print (str1)
print ('n=', n)
