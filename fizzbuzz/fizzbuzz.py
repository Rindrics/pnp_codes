def generate_fizzbuzz_msg(i):
    msg = ''
    if i % 3 == 0:
        msg += 'Fizz'
    if i % 5 == 0:
        msg += 'Buzz'
    if msg == '':
        msg += str(i)
    return msg
