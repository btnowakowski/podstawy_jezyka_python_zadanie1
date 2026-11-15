from console_io import run_menu
from zad4 import conditions, loops, puzzles

EXERCISES = {
    1: ("Liczba parzysta czy nieparzysta", conditions.even_or_odd),
    2: ("Największa z trzech liczb", conditions.largest_of_three),
    3: ("Silnia (pętla while)", loops.factorial_while),
    4: ("Od 1 do 100: podzielne przez 3, ale nie przez 5", loops.divisible_by_3_not_5),
    5: ("Sumowanie liczb do słowa stop", loops.sum_until_stop),
    6: ("Pierwsza liczba większa niż 10", loops.find_first_greater_than_10),
    7: ("Czy liczba jest pierwsza?", puzzles.check_prime),
    8: ("Liczby 1-20, co czwarta jako tekst", loops.numbers_to_20),
    9: ("Dodatnia, ujemna czy zero", conditions.check_sign),
    10: ("Zgadywanie liczby", puzzles.guess_number),
    11: ("Liczby 1-50 bez cyfry 3", loops.numbers_without_3),
}


def main():
    run_menu(EXERCISES)


if __name__ == "__main__":
    main()
