def legendre_symbol(a, p):
    """Вычисление символа Лежандра (a|p)."""
    ls = pow(a, (p - 1) // 2, p)
    return ls

def solve_quadratic_congruence(a, m):
    """Решение квадратичного сравнения x^2 ≡ a (mod m)."""
    print(f"Решаем квадратичное сравнение x^2 ≡ {a} (mod {m})")

    legendre = legendre_symbol(a, m)
    print(f"Символ Лежандра ({a}|{m}) = {legendre}")

    if legendre == -1:
        print("Квадратичное сравнение не имеет решений.")
        return
    elif legendre == 0:
        print("Квадратичное сравнение имеет бесконечно много решений.")
        return
    else:
        print("Квадратичное сравнение имеет два решения.")

        # Решение квадратичного сравнения при помощи метода корней квадратных вычетов
        roots = []
        for x in range(1, m):
            if pow(x, 2, m) == a:
                roots.append(x)

        print("Решения:")
        for root in roots:
            print(f"x ≡ {root} (mod {m})")

# Пример использования:
solve_quadratic_congruence(4, 14)
