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
    print(player + ': ' + msg)
