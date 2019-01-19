import math
a = input("переменная А")

print("перменная " + str(a))

b = input("переменная Б")

print("перменная " + str(b))

c = input("переменная С")

print("перменная " + str(c))

M = float(float(a)*float(c))

N = float(float(M)*4)

L = float(float(b)**2)

D = float(float(L)-float(N))
round(D, 2)

print(" Ответ:" + str(D))

