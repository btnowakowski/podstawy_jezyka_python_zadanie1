from zad1 import basics, booleans, floats, integers, strings, variables

EXERCISES = {
    1: ("Import this", basics.import_this),
    2: ("Pierwsze trzy zasady Zen of Python", basics.zen_first_three),
    3: ("Tekst „Python jest czytelny i prosty!”", basics.hello),
    4: ("Zmienne: imię, wiek, miasto", variables.name_age_city),
    5: ("Typ zmiennej x = 10.5", variables.type_of_float),
    6: ("Konwersja 7 na float i str", variables.convert_seven),
    7: ("Imię podane przez użytkownika", variables.ask_name),
    8: ("Słowo „super” przez indeksowanie", strings.slice_word),
    9: ("Łączenie ciągów operatorem +", strings.concatenate),
    10: ("„python” wielkimi literami", strings.to_upper),
    11: ("Litera „a” w „Ala ma kota”", strings.count_letter_a),
    12: ("Odwracanie napisu", strings.reverse_input),
    13: ("Suma, różnica, iloczyn, iloraz 15 i 4", integers.arithmetic),
    14: ("Czy liczba jest parzysta?", integers.check_even),
    15: ("Lista liczb od 1 do 10", integers.one_to_ten),
    16: ("Czy liczba jest podzielna przez 3?", integers.check_divisible_by_3),
    17: ("Pole koła dla r = 5", floats.circle),
    18: ("7 / 3 zaokrąglone do 2 miejsc", floats.divide_and_round),
    19: ("Średnia trzech liczb", floats.average_of_three),
    20: ("Czy liczba jest większa niż 10?", booleans.greater_than_ten),
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
