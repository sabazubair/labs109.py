def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

# PASSED


def is_ascending(items):
    return all(i < j for i, j in zip(items, items[1:]))

# 1. PASSED


def only_odd_digits(n):
    return set(str(n))-set('13579') == set()


# 2. Failing, Test #17


def only_odd_digits(n):
    for n in str(n):
        if (int(n) % 2 != 0):
            print(True)
            return True
    return False


only_odd_digits(10)
