from console_io import read_number

PI = 3.14


def circle_area(radius):
    return PI * radius ** 2


def circle():
    print(f"Pole koła: {circle_area(5)}")


def divide_and_round():
    print(round(7 / 3, 2))


def average_of_three():
    numbers = [read_number(f"Podaj liczbę {i}: ") for i in (1, 2, 3)]
    print(f"Średnia: {sum(numbers) / len(numbers):.2f}")
