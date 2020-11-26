def baisu(multi, n):
    count = 1
    out = 0
    i = 1
    while count <= n:
        candidate = i * multi
        if candidate_meets_condition_of_baisu(multi, candidate):
            out = candidate
            count += 1
        i += 1
    return out


def baisu2(multi, n):
    if multi not in [3, 5, 15]:
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
        elif multi == 15:
                out.append(candidate)
        i += 1
    return out


def candidate_meets_condition_of_baisu(baisu, candidate):
    condition_dic = {3: all([candidate % 3 == 0,
                             candidate % 5 != 0,
                             candidate != 12 and candidate != 34]),
                     5: all([candidate % 5 == 0,
                             candidate % 3 != 0,
                             candidate != 12 and candidate != 34]),
                     15: candidate % 15 == 0,
                     'renban': candidate == 12 or candidate == 34}
    try:
        return condition_dic[baisu]
    except KeyError:
        raise Exception("Behavior for 'baisu={baisu}' is not defined."
                        .format(baisu=baisu))


def consecutive(n):
    out = [12]
    if n > 1:
        out.append(34)
    return out


def others(n):
    out = [1]
    i = 2
    while len(out) < n:
        candidate = i
        is_baisu_n = [candidate_meets_condition_of_baisu(n, candidate) for n in [3, 5, 15]]
        is_renban = candidate_meets_condition_of_baisu('renban', candidate)
        if all([not any(is_baisu_n), not is_renban]):
            out.append(candidate)
        i += 1
    return out[-1]


if __name__ == '__main__':
    print('Multiple of 3s:')
    for i in range(1, 20):
        print(str(baisu(3, i)))

    print('Multiple of 5s:')
    for i in range(1, 20):
        print(str(baisu(5, i)))

    print('Multiple of 15s:')
    for i in range(1, 20):
        print(str(baisu(15, i)))

    print('Others:')
    for i in range(1, 20):
        print(str(others(i)))
