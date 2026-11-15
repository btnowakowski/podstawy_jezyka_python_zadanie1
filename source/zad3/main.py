from console_io import run_menu
from zad3 import everyday, numbers, triangle

EXERCISES = {
    1: ("Trzy liczby: największa, najmniejsza, średnia, parzystość sumy", numbers.three_numbers),
    2: ("Czas trwania filmu", everyday.film_duration),
    3: ("Trójkąt z trzech boków", triangle.check_triangle),
    4: ("Silnia ze sprawdzaniem danych", numbers.factorial_with_checks),
    5: ("Wypłata: nadgodziny i podatek", everyday.payday),
}


def main():
    run_menu(EXERCISES)


if __name__ == "__main__":
    main()
