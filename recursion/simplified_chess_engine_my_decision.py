from itertools import product


def knight_moves(position):
    x, y = position
    moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
    moves = [(x, y) for x, y in moves if 1 <= x < 5 and 1 <= y < 5]
    return moves


def bishop_moves(position):
    x, y = position
    moves = []
    for i in range(1, 5):
        moves.append(list(product([x-i, x+i], [y-i, y+i])))
    moves = [(x, y) for x, y in moves if 1 <= x < 5 and 1 <= y < 5]
    return moves


def simplifiedChessEngine(whites, blacks, moves):
    pass


if __name__ == '__main__':
    # g = int(input())
    #
    # for _ in range(g):
    #     wbm = input().split()
    #     w = int(wbm[0])
    #     b = int(wbm[1])
    #     m = int(wbm[2])
    #     whites = [list(map(lambda x: x[0], input().rstrip().split())) for _ in range(w)]
    #     blacks = [list(map(lambda x: x[0], input().rstrip().split())) for _ in range(b)]
        # simplifiedChessEngine(whites, blacks, m)

    g = 1
    w = 2
    b = 1
    m = 1
    whites = [['N', 'B', '2'], ['Q', 'B', '1']]
    blacks = [['Q', 'A', '4']]

    dict_letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    chessboard = {}
    for row in range(4, 0, -1):
        for col in range(1, 5):
            chessboard[(col, row, None)] = None
    for white in whites:
        white[1] = dict_letters[white[1]]
        chessboard[(white[1], int(white[2]), None)] = white[0]
        chessboard[(white[1], int(white[2]), 'w')] = chessboard.pop((white[1], int(white[2]), None))
    for black in blacks:
        black[1] = dict_letters[black[1]]
        chessboard[(black[1], int(black[2]), None)] = black[0]
        chessboard[(black[1], int(black[2]), 'b')] = chessboard.pop((black[1], int(black[2]), None))
    print(chessboard)
    simplifiedChessEngine(whites, blacks, m)
    print(knight_moves((2, 2)))
    print(bishop_moves((2, 2)))
    print(knight_moves((2, 2)))

