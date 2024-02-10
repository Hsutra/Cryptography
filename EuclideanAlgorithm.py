import math
#Реализовать программный продукт решения диофантового
#уравнения первой степени с помощью расширенного алгоритма
#Евклида с указанием всех промежуточных результатов.
# ax + bx = c

def euclideanAlgorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = euclideanAlgorithm(b, a % b)
        return gcd, y, x - (a // b) * y

def resolveEquation(a, b, c):
    gcd, x, y = euclideanAlgorithm(a, b)
    if c % gcd != 0:
        return "Решения нет"
    else:
        x *= c // gcd
        y *= c // gcd
        return x, y

a = 5
b = 7
c = 14
res = resolveEquation(a, b, c)
print(f"Решение уравнения: {a}x + {b}y = {c} равно {res}.")

