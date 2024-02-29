'''
Вариант 5. Реализовать программный продукт решения диофантового
уравнения первой степени с помощью расширенного алгоритма
Евклида.
'''

def euclideanAlgorithm(a, b, i = 1):
    if b == 0:
        return a, 1, 0
    else:
        print(f"q{i} = {a}, r{i} = {b}")
        gcd, x, y = euclideanAlgorithm(b, a % b, i + 1)
        print(f"({b}) -> {x}, ({a}) -> {y}")
        return gcd, y, x - (a // b) * y

def resolveEquation(a, b, c):
    gcd, x, y = euclideanAlgorithm(a, b)
    if c % gcd != 0:
        return None
    else:
        x *= c // gcd
        y *= c // gcd
        return x, y, gcd
#
# a = 5
# b = 7
# c = 14
# res = resolveEquation(a, b, c)
# if res:
#     commRes = f"x = {res[0]} + {b // res[2]}k, y = {res[1]} - {a // res[2]}k"
#     print(f"Решение уравнения {a}x + {b}y = {c}:\nЧастное решение: x = {res[0]}, y = {res[1]}\nОбщее решение: {commRes}")
# else:
#     print("Решения нет")


def extended_euclidean_algorithm(a, b):
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    i = 1

    while r2 != 0:
        print(f"Итерация {i}:\nr1 = {r1}, r2 = {r2}, s1 = {s1}, s2 = {s2}, t1 = {t1}, t2 = {t2}")
        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2

        r1, r2 = r2, r
        s1, s2 = s2, s
        t1, t2 = t2, t
        i += 1
    return r1, s1, t1

def diophantine_equation(a, b, c):
    d, s, t = extended_euclidean_algorithm(a, b)
    if c % d != 0:
        return None
    k = c // d
    x = s * k
    y = t * k
    return d, x, y

# Пример использования
a = 7
b = 5
c = 14
solution = diophantine_equation(a, b, c)
if solution:
    d, x, y = solution
    comm_solution = f"x = {x} + {b // d}t, y = {y} - {a // d}t"
    print(f"Решение уравнения {a}x + {b}y = {c}:\nЧастное решение: x = {x}, y = {y}\nОбщее решение: {comm_solution}")
else:
    print("Уравнение не имеет решения")
