ZEN_FIRST_THREE = [
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
]


def import_this():
    # the import itself prints the text, and only the first time
    import this


def zen_first_three():
    for number, rule in enumerate(ZEN_FIRST_THREE, start=1):
        print(f"{number}. {rule}")


def hello():
    print("Python jest czytelny i prosty!")
