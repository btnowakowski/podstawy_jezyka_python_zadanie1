from console_io import read_int


def arithmetic():
    a, b = 15, 4
    print(f"Suma: {a + b}")
    print(f"Różnica: {a - b}")
    print(f"Iloczyn: {a * b}")
    print(f"Iloraz: {a / b}")


def is_even(number):
    return number % 2 == 0


def is_divisible_by_3(number):
    return number % 3 == 0


def check_even():
    number = read_int("Podaj liczbę: ")
    print("Parzysta" if is_even(number) else "Nieparzysta")


def one_to_ten():
    print(list(range(1, 11)))


def check_divisible_by_3():
    number = read_int("Podaj liczbę: ")
    if is_divisible_by_3(number):
        print(f"{number} jest podzielna przez 3")
    else:
        print(f"{number} nie jest podzielna przez 3")
