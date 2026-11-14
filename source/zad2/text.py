from console_io import read_int


def count_non_space(text):
    return len("".join(text.split()))


def is_password_valid(password):
    return len(password) >= 8 and any(ch.isdigit() for ch in password)


def greeting():
    name = input("Jak masz na imię? ").strip()
    print(f"Cześć, {name}! Miło Cię widzieć!")


def count_chars():
    sentence = input("Wpisz zdanie: ")
    print(f"Liczba znaków (bez spacji): {count_non_space(sentence)}")


def check_password():
    if is_password_valid(input("Hasło: ")):
        print("Hasło jest poprawne.")
    else:
        print("Hasło musi mieć co najmniej 8 znaków i zawierać cyfrę.")


def repeat_word():
    word = input("Podaj słowo: ")
    times = read_int("Ile razy powtórzyć? ")
    print(word * max(times, 0))


def quiz():
    while read_int("Ile to 2 + 2? ") != 4:
        print("Spróbuj ponownie!")
    print("Dobrze!")
