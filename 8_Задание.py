import math
F = input("переменная F")

print("перменная " + str(F))

U = input("переменная U")

print("перменная " + str(U))

a = input("переменная a")

print("перменная " + str(a))

H = math.cos(float(a))

P = float(float(F) * float(U) * float(H))
M = round(P, 3)
print("Ответ "+str(M))
