from console_io import read_int


def first_greater_than(numbers, limit):
    for number in numbers:
        if number > limit:
            return number
    return None


def has_digit_3(number):
    return "3" in str(number)


def factorial_while():
    n = read_int("Podaj liczbę: ")
    if n < 0:
        print("Silnia nie jest określona dla liczb ujemnych.")
        return
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    print(f"{n}! = {result}")


def divisible_by_3_not_5():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 != 0:
            print(number)


def sum_until_stop():
    total = 0
    while True:
        text = input("Liczba (lub stop): ").strip()
        if text.lower() == "stop":
            break
        try:
            total += float(text.replace(",", "."))
        except ValueError:
            print("To nie jest liczba.")
    print(f"Suma: {total:g}")


def find_first_greater_than_10():
    text = input("Liczby oddzielone spacją (Enter = 1-100): ").split()
    try:
        numbers = [int(x) for x in text] if text else list(range(1, 101))
    except ValueError:
        print("Podaj same liczby całkowite.")
        return
    found = first_greater_than(numbers, 10)
    print(f"Pierwsza liczba większa niż 10: {found}" if found is not None else "Nie ma takiej liczby.")


def numbers_to_20():
    for number in range(1, 21):
        if number % 4 == 0:
            print("divisible by 4")
        else:
            print(number)


def numbers_without_3():
    for number in range(1, 51):
        if not has_digit_3(number):
            print(number)
