from console_io import read_number


def can_build(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a + b > c and a + c > b and b + c > a


def kind(a, b, c):
    if a == b == c:
        return "równoboczny"
    if a == b or b == c or a == c:
        return "równoramienny"
    return "różnoboczny"


def check_triangle():
    a = read_number("Bok a: ")
    b = read_number("Bok b: ")
    c = read_number("Bok c: ")
    if not can_build(a, b, c):
        print("Z takich boków nie da się zbudować trójkąta.")
    else:
        print(f"Da się zbudować trójkąt, jest {kind(a, b, c)}.")
