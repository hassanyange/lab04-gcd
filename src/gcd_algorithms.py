#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Лабораторная работа №4
Вычисление наибольшего общего делителя
Реализация алгоритмов:
1. Алгоритм Евклида
2. Бинарный алгоритм Евклида  
3. Расширенный алгоритм Евклида
4. Расширенный бинарный алгоритм Евклида
"""

def euclidean_algorithm(a, b):
    """
    Классический алгоритм Евклида
    Вход: a, b - целые числа, 0 < b <= a
    Выход: НОД(a, b)
    """
    r0, r1 = a, b
    i = 1
    
    while True:
        ri_plus_1 = r0 % r1
        if ri_plus_1 == 0:
            return r1
        r0, r1 = r1, ri_plus_1
        i += 1

def binary_euclidean_algorithm(a, b):
    """
    Бинарный алгоритм Евклида
    Вход: a, b - целые числа, 0 < b <= a
    Выход: НОД(a, b)
    """
    g = 1
    
    # Шаг 2: Выносим общие степени двойки
    while a % 2 == 0 and b % 2 == 0:
        a = a // 2
        b = b // 2
        g = 2 * g
    
    u, v = a, b
    
    # Шаг 4: Основной цикл
    while u != 0:
        # Шаг 4.1: Делим u на 2 пока четное
        while u % 2 == 0:
            u = u // 2
        
        # Шаг 4.2: Делим v на 2 пока четное  
        while v % 2 == 0:
            v = v // 2
        
        # Шаг 4.3: Вычитаем
        if u >= v:
            u = u - v
        else:
            v = v - u
    
    # Шаг 5: Результат
    return g * v

def extended_euclidean_algorithm(a, b):
    """
    Расширенный алгоритм Евклида
    Вход: a, b - целые числа, 0 < b <= a
    Выход: (d, x, y) где d = НОД(a, b) и ax + by = d
    """
    r0, r1 = a, b
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    i = 1
    
    while True:
        # Деление с остатком
        qi = r0 // r1
        ri_plus_1 = r0 % r1
        
        if ri_plus_1 == 0:
            d = r1
            x = x1
            y = y1
            return d, x, y
        
        # Вычисление новых коэффициентов
        xi_plus_1 = x0 - qi * x1
        yi_plus_1 = y0 - qi * y1
        
        # Обновление переменных
        r0, r1 = r1, ri_plus_1
        x0, x1 = x1, xi_plus_1
        y0, y1 = y1, yi_plus_1
        i += 1

def extended_binary_euclidean_algorithm(a, b):
    """
    Расширенный бинарный алгоритм Евклида
    Вход: a, b - целые числа, 0 < b <= a
    Выход: (d, x, y) где d = НОД(a, b) и ax + by = d
    """
    original_a, original_b = a, b
    g = 1
    
    # Шаг 2: Выносим общие степени двойки
    while a % 2 == 0 and b % 2 == 0:
        a = a // 2
        b = b // 2
        g = 2 * g
    
    u, v = a, b
    A, B, C, D = 1, 0, 0, 1
    
    # Шаг 4: Основной цикл
    while u != 0:
        # Шаг 4.1: Обработка u
        while u % 2 == 0:
            u = u // 2
            if A % 2 == 0 and B % 2 == 0:
                A = A // 2
                B = B // 2
            else:
                A = (A + original_b) // 2
                B = (B - original_a) // 2
        
        # Шаг 4.2: Обработка v
        while v % 2 == 0:
            v = v // 2
            if C % 2 == 0 and D % 2 == 0:
                C = C // 2
                D = D // 2
            else:
                C = (C + original_b) // 2
                D = (D - original_a) // 2
        
        # Шаг 4.3: Сравнение и вычитание
        if u >= v:
            u = u - v
            A = A - C
            B = B - D
        else:
            v = v - u
            C = C - A
            D = D - B
    
    # Шаг 5: Результат
    d = g * v
    x, y = C, D
    return d, x, y

def test_algorithms():
    """
    Тестирование алгоритмов на примерах из лабораторной работы
    """
    test_cases = [
        (12345, 24690, 12345),
        (12345, 54321, 3),
        (12345, 12541, 1),
        (91, 105, 7),
        (48, 18, 6)
    ]
    
    print("Тестирование алгоритмов вычисления НОД")
    print("=" * 50)
    
    for a, b, expected in test_cases:
        print(f"НОД({a}, {b}) = {expected}")
        
        # Алгоритм Евклида
        result1 = euclidean_algorithm(a, b)
        print(f"  Алгоритм Евклида: {result1} {'✓' if result1 == expected else '✗'}")
        
        # Бинарный алгоритм Евклида
        result2 = binary_euclidean_algorithm(a, b)
        print(f"  Бинарный алгоритм: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Расширенный алгоритм Евклида
        d3, x3, y3 = extended_euclidean_algorithm(a, b)
        print(f"  Расширенный алгоритм: {d3} (коэффициенты: {a}*{x3} + {b}*{y3} = {d3}) {'✓' if d3 == expected else '✗'}")
        
        # Расширенный бинарный алгоритм
        d4, x4, y4 = extended_binary_euclidean_algorithm(a, b)
        print(f"  Расшир. бинарный: {d4} (коэффициенты: {a}*{x4} + {b}*{y4} = {d4}) {'✓' if d4 == expected else '✗'}")
        
        # Проверка линейного представления
        check1 = a * x3 + b * y3 == d3
        check2 = a * x4 + b * y4 == d4
        print(f"  Проверка линейного представления: Алг.Евклида {'✓' if check1 else '✗'}, Бинарный {'✓' if check2 else '✗'}")
        
        print()

if __name__ == "__main__":
    test_algorithms()
    
    # Дополнительное тестирование с вводом пользователя
    print("\nДополнительное тестирование")
    print("Введите два числа для вычисления НОД:")
    try:
        a = int(input("Первое число (a): "))
        b = int(input("Второе число (b): "))
        
        if b > a:
            a, b = b, a  # Меняем местами, чтобы a >= b
        
        print(f"\nРезультаты для НОД({a}, {b}):")
        print(f"Алгоритм Евклида: {euclidean_algorithm(a, b)}")
        print(f"Бинарный алгоритм: {binary_euclidean_algorithm(a, b)}")
        
        d, x, y = extended_euclidean_algorithm(a, b)
        print(f"Расширенный алгоритм: {d} (коэффициенты: {a}*{x} + {b}*{y} = {d})")
        
        d_bin, x_bin, y_bin = extended_binary_euclidean_algorithm(a, b)
        print(f"Расшир. бинарный: {d_bin} (коэффициенты: {a}*{x_bin} + {b}*{y_bin} = {d_bin})")
        
    except ValueError:
        print("Ошибка: введите целые числа!")