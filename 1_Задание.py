import math
a = input("переменная А")

print("перменная " + str(a))

b = input("переменная Б")

print("перменная " + str(b))

c = input("переменная С")

print("перменная " + str(c))

H = float(float(b) ** 2 - 4 * float(a) * float(c))

P = round(float(H), 2)

print("Ответ "+str(P))
