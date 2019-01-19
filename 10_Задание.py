import math
V = input("переменная V")

print("перменная " + str(V))

J = input("переменная J")

print("перменная " + str(J))

c = input("переменная С")

print("перменная " + str(c))

Y = (1-(float(V)**2)/(float(c)**2))

F = math.sqrt(float(Y))

P = int(float(J)*float(F))
print("Ответ "+str(P))
