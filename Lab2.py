import math
import re


def task1():
    print("Завдання 1")

    a = float(input("Введіть значення a (a != 0): "))
    while a == 0:
        print("Значення 'a' не може дорівнювати 0")
        a = float(input("Введіть значення a (a != 0): "))

    eps = float(input("Введіть точність epsilon: "))
    while eps <= 0:
        print("Epsilon має бути більше 0")
        eps = float(input("Введіть точність epsilon: "))

    total_sum = 0.0
    k = 1
    count = 0

    while True:
        term = math.exp(-k) / (a ** (2 * k) + math.factorial(k))

        if term < eps:
            break

        total_sum += term
        count += 1
        k += 1

    print(f"Сума: {total_sum}")
    print(f"Кількість врахованих доданків: {count}\n")


def task2():
    print("Завдання 2")
    x = float(input("Введіть x (x != 0): "))
    eps = float(input("Введіть точність epsilon: "))

    a_prev = x
    found = False

    for n in range(1, 103):
        a_curr = (a_prev + 1) / (a_prev + 2) + (x ** 2) / a_prev

        if abs(a_curr - a_prev) < eps:
            print(f"Знайдено член a_{n} = {a_curr}")
            print(f"Номер члена n = {n}\n")
            found = True
            break

        a_prev = a_curr

    if not found:
        print("Умову не було досягнуто за перші 102 члени послідовності.\n")


def task3():
    print("Завдання 3")
    text = input("Введіть текст: ")
    word1 = input("Введіть слово, яке треба замінити: ")
    word2 = input("Введіть нове слово: ")

    pattern = r'\b' + re.escape(word1) + r'\b'
    result_text = re.sub(pattern, word2, text)

    print("Результат:")
    print(result_text, "\n")


def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


def task4():
    print("Завдання 4")
    n = int(input("Введіть натуральне число N: "))
    if n <= 0:
        print("Число має бути натуральним.")
        return

    result = sum_of_digits(n)
    print(f"Сума цифр числа {n}: {result}")


def main_menu():
    while True:
        print("\nГОЛОВНЕ МЕНЮ")
        print("1 - Завдання 1")
        print("2 - Завдання 2")
        print("3 - Завдання 3")
        print("4 - Завдання 4")
        print("0 - Вихід")

        choice = input("Виберіть дію: ")

        match choice:
            case "1":
                task1()
            case "2":
                task2()
            case "3":
                task3()
            case "4":
                task4()
            case "0":
                print("До побачення!")
                break
            case _:
                print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()
