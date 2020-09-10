players = ['A', 'B', 'C', 'D', 'E', 'F']
n_round = 3

for i, player in enumerate(players * n_round):
    turn = i + 1
    msg = player + ': '
    if turn % 3 == 0 or turn % 5 == 0:
        if turn % 3 == 0:
            msg = msg + 'Fizz'
        if turn % 5 == 0:
            msg = msg + 'Buzz'
    else:
        msg = msg + str(turn)
    print(msg)
