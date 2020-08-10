data = {
    70:'armadillo',
    55:'ant',
    140:'yak',
    1041:'parrot',
    20:'bat',
    150:'yak'
}

def mathify(a, b):
    if a* 2 > b / 2:
        return a
    return b

def is_game_over(tictac):
    # 3x3

    # x_won = ['X', 'X', 'X']
    # o_won = ['O', 'O', 'O']
    # for i in tictac:
    #     if i == x_won:
    #         print('X has won!')
    #     elif i == o_won:
    #         print('O has won!')
    # for i in range(1, 4):
    #     if tictac[i][i-1] == 'X' and tictac[i-1][i-1] =='X' and tictac[i+1][i-1] == 'X':
    #         print('X has won!')
    #     elif tictac[i][i-1] == 'O' and tictac[i-1][i-1] =='O' and tictac[i+1][i-1] == 'O':
    #         print('O has won!')
    #     else:
    #         print('there is a draw')
    for i in range(3):
        # check col
        if tictac[i][0] == tictac[i][1] and tictac[i][1] == tictac[i][2]:
            return True
        # check row 
        if tictac[0][i] == tictac[1][i] and tictac[1][i] == tictac[2][i]:
            return True
        return False

tic = [
    ['x','x','o'],
    ['o','o','o'],
    ['o', 'o','x']
]




def main():
    string = 'z'
    number = 20
    tracker = 0
    for k,v in data.items():
        res = mathify(number, k)
        if res > 100:
            string = v
        tracker = mathify(k, number)
        number += 30
        print('string:', string)
        print('number:', number)
        print('tracker:', tracker)

        print('iter')
# main()

print(is_game_over(tic))
