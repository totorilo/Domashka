import math
print("Введите числа")

R = input("переменная R")

print("перменная " + str(R))

r = input("переменная r")

print("перменная " + str(r))

Y = float(float(R)**2 - float(r)**2)

S = float(3.14 * float(Y))

round(float(S), 2)

print("Площадь = "+str(S))
