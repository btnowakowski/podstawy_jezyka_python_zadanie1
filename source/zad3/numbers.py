from console_io import read_int

MAX_FACTORIAL_N = 20


def analyze(a, b, c):
    # no max() / min(), just comparisons
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    mean = (a + b + c) / 3
    sum_is_even = (a + b + c) % 2 == 0
    return largest, smallest, mean, sum_is_even


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def three_numbers():
    a = read_int("Pierwsza liczba: ")
    b = read_int("Druga liczba: ")
    c = read_int("Trzecia liczba: ")
    largest, smallest, mean, sum_is_even = analyze(a, b, c)
    print(f"Największa: {largest}")
    print(f"Najmniejsza: {smallest}")
    print(f"Średnia: {mean:.2f}")
    print("Suma jest parzysta" if sum_is_even else "Suma jest nieparzysta")


def factorial_with_checks():
    n = read_int("Podaj n: ")
    if n < 0:
        print("Silnia nie jest określona dla liczb ujemnych.")
    elif n > MAX_FACTORIAL_N:
        print(f"Uwaga: {n} to za dużo, wynik byłby ogromny (limit to {MAX_FACTORIAL_N}).")
    else:
        print(f"{n}! = {factorial(n)}")
