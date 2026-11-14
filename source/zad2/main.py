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
    for number, (title, _) in EXERCISES.items():
        print(f"{number:>2}. {title}")
    while True:
        choice = input("\nNumer ćwiczenia (Enter kończy): ").strip()
        if not choice:
            break
        if choice.isdigit() and int(choice) in EXERCISES:
            print()
            EXERCISES[int(choice)][1]()
        else:
            print("Nie ma takiego ćwiczenia.")


if __name__ == "__main__":
    main()
