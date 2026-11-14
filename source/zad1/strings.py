def slice_word():
    text = "Python jest super!"
    print(text[12:17])


def concatenate():
    print("Witaj, " + "świecie!")


def to_upper():
    print("python".upper())


def count_letter_a():
    # lower() so the big A in Ala is counted too
    print("Ala ma kota".lower().count("a"))


def reverse_input():
    text = input("Podaj napis do odwrócenia: ")
    print(text[::-1])
