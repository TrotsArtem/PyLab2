import math

def task1():


def task2():


def task3():


def task4():


def main_menu():
    while True:
        print("\n=== ГОЛОВНЕ МЕНЮ ===")
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