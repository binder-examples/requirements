def add_two_numbers(a, b):
    return a + b


def subtract_two_numbers(a, b):
    if b > a:
        raise ValueError("Cannot go negative for some reason!")
    return a - b
