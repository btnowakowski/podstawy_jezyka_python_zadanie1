def read_number(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("To nie jest poprawna liczba, spróbuj ponownie.")


def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Podaj liczbę całkowitą.")


def run_menu(exercises):
    for number, (title, _) in exercises.items():
        print(f"{number:>2}. {title}")
    while True:
        choice = input("\nNumer ćwiczenia (Enter kończy): ").strip()
        if not choice:
            break
        if choice.isdigit() and int(choice) in exercises:
            print()
            exercises[int(choice)][1]()
        else:
            print("Nie ma takiego ćwiczenia.")
