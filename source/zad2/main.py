from console_io import run_menu
from zad2 import numbers, text

EXERCISES = {
    1: ("Konwersja temperatur", numbers.temperature),
    2: ("Liczba parzysta czy nieparzysta?", numbers.even_or_odd),
    3: ("Kalkulator wieku", numbers.age),
    4: ("Generator powitania", text.greeting),
    5: ("Liczenie znaków w tekście", text.count_chars),
    6: ("Kalkulator średniej", numbers.average),
    7: ("Sprawdzanie hasła", text.check_password),
    8: ("Porównywanie dwóch liczb", numbers.compare_numbers),
    9: ("Mnożenie tekstu", text.repeat_word),
    10: ("Prosty test logiczny", text.quiz),
    11: ("Prosty kalkulator", numbers.calculator),
}


def main():
    run_menu(EXERCISES)


if __name__ == "__main__":
    main()
