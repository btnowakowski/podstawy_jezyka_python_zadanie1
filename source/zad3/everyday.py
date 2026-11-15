from console_io import read_int, read_number

SHORT_FILM_LIMIT = 90
HOURLY_RATE = 20
NORMAL_HOURS = 40
OVERTIME_MULTIPLIER = 1.5
TAX_RATE = 0.19


def hours_and_minutes(total_minutes):
    return total_minutes // 60, total_minutes % 60


def gross_pay(hours):
    if hours <= NORMAL_HOURS:
        return hours * HOURLY_RATE
    overtime = hours - NORMAL_HOURS
    return NORMAL_HOURS * HOURLY_RATE + overtime * HOURLY_RATE * OVERTIME_MULTIPLIER


def film_duration():
    minutes = read_int("Czas trwania filmu w minutach: ")
    if minutes < 0:
        print("Czas nie może być ujemny.")
        return
    hours, rest = hours_and_minutes(minutes)
    print(f"Film trwa {hours} godzin i {rest} minut")
    answer = input("Czy obejrzysz cały film? (tak/nie): ").strip().lower()
    if answer == "tak":
        print("krótki film" if minutes < SHORT_FILM_LIMIT else "długi film")


def payday():
    hours = read_number("Ile godzin przepracowano? ")
    if hours < 0:
        print("Liczba godzin nie może być ujemna.")
        return
    gross = gross_pay(hours)
    tax = gross * TAX_RATE
    print(f"Brutto: {gross:.2f} zł")
    print(f"Podatek 19%: {tax:.2f} zł")
    print(f"Netto: {gross - tax:.2f} zł")
