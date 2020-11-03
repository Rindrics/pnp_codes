def baisu(multi, n):
    if multi not in [3, 5]:
        raise Exception("Behavior for 'multi={multi}' is not defined."
                        .format(multi=multi))
    out = [multi]
    i = 2
    while len(out) < n:
        candidate = i * multi
        if multi == 3:
            if candidate % 5 != 0 and candidate != 12:
                out.append(candidate)
        elif multi == 5:
            if candidate % 3 != 0 and candidate != 12:
                out.append(candidate)
        i += 1
    return out


def baisu_3(n):
    multi = 3
    out = [multi]
    i = 2
    while len(out) < n:
        candidate = i * multi
        if candidate % 5 != 0 and candidate != 12:
            out.append(candidate)
        i += 1
    return out


def baisu_5(n):
    multi = 5
    out = [multi]
    i = 2
    while len(out) < n:
        candidate = i * multi
        if candidate % 3 != 0:
            out.append(candidate)
        i += 1
    return out

# def multiple_of_15(n):
#     out = [15]
#     i   = 2
#     while len(out) < n:
#         multi = i * 15
#         out.append(multi)
#         i += 1
#     return out

# def consecutive(n):
#     out = [12]
#     if n > 1:
#         out.append(34)
#     return out

# def others(n):
#     out = [1]
#     i   = 2
#     while len(out) < n:
#         specials = set(multiple_of_3(i)) ^ set(multiple_of_5(i)) ^ set(multiple_of_15(i)) ^ set(consecutive(i))
#         out = set(range(1, i)) - specials
#         i += 1

#     return list(out)

# if __name__ == '__main__':
#     print(multiple_of_3(n=1))
#     print(multiple_of_3(n=2))
#     print(multiple_of_3(n=3))

#     print(multiple_of_5(n=1))
#     print(multiple_of_5(n=2))
#     print(multiple_of_5(n=3))

#     print(multiple_of_15(n=1))
#     print(multiple_of_15(n=2))
#     print(multiple_of_15(n=3))

#     print(consecutive(n=1))
#     print(consecutive(n=2))
