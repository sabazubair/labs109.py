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


def is_ascending(items):
    return all(i < j for i, j in zip(items, items[1:]))


def only_odd_digits(n):
    return set(str(n))-set('13579') == set()


def squares_intersect(s1, s2):
    (x1, y1, d1) = s1
    (x2, y2, d2) = s2
    return not (x1 + d1 < x2 or x2 + d2 < x1 or y1 + d1 < y2 or y2 + d2 < y1)


def tukeys_ninthers(items):
    while len(items) > 1:
        items = [sorted(items[i:i+3])[1] for i in range(0, len(items), 3)]
    return items[0]


def knight_jump(steps, start, end):
    return steps == tuple(sorted((abs(x - y) for (x, y) in zip(start, end)), reverse=True))


def nearest_smaller(items):
    n, result = len(items), []
    for (i, e) in enumerate(items):
        j = 1
        while j < n:
            left = items[i - j] if i >= j else e
            right = items[i + j] if i+j < n else e
            if left < e or right < e:
                result.append(left if left < right else right)
                break
            j += 1
        else:
            result.append(e)
    return result

# # 2. Failing, Test #17


# def only_odd_digits(n):
#     for n in str(n):
#         if (int(n) % 2 != 0):
#             print(True)
#             return True
#     return False


# only_odd_digits(10)
