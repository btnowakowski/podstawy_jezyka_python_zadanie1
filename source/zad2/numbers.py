import operator
from datetime import date

from console_io import read_int, read_number

OPERATIONS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}


def celsius_to_fahrenheit(celsius):
    return 9 / 5 * celsius + 32


def age_from_year(birth_year):
    this_year = date.today().year
    if birth_year > this_year:
        return None
    return this_year - birth_year


def compare(a, b):
    if a > b:
        return f"{a:g} jest większa od {b:g}"
    if a < b:
        return f"{a:g} jest mniejsza od {b:g}"
    return "Liczby są równe"


def calculate(a, op, b):
    if op not in OPERATIONS:
        raise ValueError(f"Nieznany operator: {op}")
    if op == "/" and b == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero.")
    return OPERATIONS[op](a, b)


def temperature():
    celsius = read_number("Temperatura w °C: ")
    print(f"{celsius:g} °C = {celsius_to_fahrenheit(celsius):.1f} °F")


def even_or_odd():
    number = read_int("Podaj liczbę całkowitą: ")
    print(f"{number} jest {'parzysta' if number % 2 == 0 else 'nieparzysta'}")


def age():
    result = age_from_year(read_int("Rok urodzenia: "))
    if result is None:
        print("Rok urodzenia nie może być z przyszłości.")
    else:
        print(f"Masz {result} lat.")


def average():
    grades = [read_number(f"Ocena {i}: ") for i in (1, 2, 3)]
    print(f"Średnia: {sum(grades) / len(grades):.2f}")


def compare_numbers():
    print(compare(read_number("Pierwsza liczba: "), read_number("Druga liczba: ")))


def calculator():
    a = read_number("Pierwsza liczba: ")
    op = input("Operator (+, -, *, /): ").strip()
    b = read_number("Druga liczba: ")
    try:
        print(f"Wynik: {calculate(a, op, b):g}")
    except (ValueError, ZeroDivisionError) as exc:
        print(exc)
