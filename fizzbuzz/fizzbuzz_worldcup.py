from fizzbuzz import fizzbuzz

players = ['A', 'B', 'C', 'D', 'E', 'F']
n_round = 3

for i, player in enumerate(players * n_round):
    turn = i + 1
    msg = player + ': ' + fizzbuzz(turn)
    print(msg)
