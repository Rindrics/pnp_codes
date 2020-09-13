players = ['A', 'B', 'C', 'D']
n_round = 3

for i, player in enumerate(players * n_round):
    turn = i + 1
    msg  = ''
    if turn % 3 == 0:
        msg += 'Fizz'
    if turn % 5 == 0:
        msg += 'Buzz'
    if msg == '':
        msg += str(turn)
    if str(turn) == '12' or str(turn) == '23':
        msg += '連番!'
    print(player + ': ' + msg)
