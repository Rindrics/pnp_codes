def generate_call(i):
    msg = ''
    if i % 3 == 0:
        msg += 'Fizz'
    if i % 5 == 0:
        msg += 'Buzz'

    if str(i) == '12' or str(i) == '34':
        msg = str(i) + '連番!'
    else:
        if msg == '':
            msg += str(i)
    return msg
