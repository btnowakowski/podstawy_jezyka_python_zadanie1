from console_io import read_int


def sign(number):
    if number > 0:
        return "dodatnia"
    if number < 0:
        return "ujemna"
    return "równa zero"


def even_or_odd():
    number = read_int("Podaj liczbę: ")
    if number % 2 == 0:
        print("Parzysta")
    else:
        print("Nieparzysta")


def largest_of_three():
    a = read_int("Pierwsza liczba: ")
    b = read_int("Druga liczba: ")
    c = read_int("Trzecia liczba: ")
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    print(f"Największa: {largest}")


def check_sign():
    number = read_int("Podaj liczbę: ")
    print(f"Liczba jest {sign(number)}")
