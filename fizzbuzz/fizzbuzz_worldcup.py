from fizzbuzz import generate_fizzbuzz_msg

players = ['A', 'B', 'C', 'D']
n_round = 3

for i, player in enumerate(players * n_round):
    turn = i + 1
    msg = generate_fizzbuzz_msg(turn)
    print(player + ': ' + msg)
