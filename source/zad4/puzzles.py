import random

from console_io import read_int


def is_prime(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
        if divisor * divisor > n:
            break
    return True


def check_prime():
    n = read_int("Podaj liczbę: ")
    print(f"{n} jest liczbą pierwszą" if is_prime(n) else f"{n} nie jest liczbą pierwszą")


def guess_number():
    secret = random.randint(1, 10)
    guess = read_int("Zgadnij liczbę od 1 do 10: ")
    while guess != secret:
        guess = read_int("Źle, spróbuj jeszcze raz: ")
    print("Zgadłeś!")
