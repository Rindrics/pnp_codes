def fizzbuzz(i):
    msg = ''
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0:
            msg = msg + 'Fizz'
        if i % 5 == 0:
            msg = msg + 'Buzz'
    else:
        msg = msg + str(i)
    return msg
