#!/usr/bin/python3

def cloneboard(board):
    tmp = []
    for elt in board:
        tmp.append(list(elt))
    return tmp


def dispboard(board):
    for c in board:
        print(c)
    print()


def getmoves(board, c, r):
    if board[c][r][0] == "N":
        return _getknightmoves(board, c, r)
    elif board[c][r][0] == "B":
        return _getbishopmoves(board, c, r)
    elif board[c][r][0] == "R":
        return _getrookmoves(board, c, r)
    else:  # board[c][r][0] == "Q"
        tmp1 = _getbishopmoves(board, c, r)
        tmp2 = _getrookmoves(board, c, r)
        return (tmp1[0] + tmp2[0], tmp1[1] or tmp2[1])


def _getknightmoves(board, c, r):
    moves = []
    eatqueen = False
    for i in [2, 1]:
        j = 3 - i
        for k in [1, -1]:
            for l in [1, -1]:
                newc = c + k * i
                newr = r + l * j
                if (newc in range(4)) and (newr in range(4)):  # in board range
                    if board[newc][newr] == None or board[newc][newr][1] != board[c][r][1]:
                        if board[newc][newr] != None and board[newc][newr][0] == "Q":
                            eatqueen = True
                        newboard = cloneboard(board)
                        newboard[newc][newr] = board[c][r]
                        newboard[c][r] = None
                        moves.append(newboard)
    return (moves, eatqueen)


def _getbishopmoves(board, c, r):
    moves = []
    eatqueen = False
    for k in [1, -1]:
        for l in [1, -1]:
            newc = c + k
            newr = r + l
            while (newc in range(4)) and (newr in range(4)):
                if board[newc][newr] != None and board[newc][newr][1] == board[c][r][1]:
                    break
                if board[newc][newr] != None and board[newc][newr][0] == "Q":
                    eatqueen = True
                newboard = cloneboard(board)
                eat = (board[newc][newr] != None)
                newboard[newc][newr] = board[c][r]
                newboard[c][r] = None
                moves.append(newboard)
                if eat:
                    break
                newc += k
                newr += l
    return (moves, eatqueen)


def _getrookmoves(board, c, r):
    moves = []
    eatqueen = False
    for k in [1, -1]:
        newc = c + k
        while newc in range(4):
            if board[newc][r] != None and board[newc][r][1] == board[c][r][1]:
                break
            if board[newc][r] != None and board[newc][r][0] == "Q":
                eatqueen = True
            eat = (board[newc][r] != None)
            newboard = cloneboard(board)
            newboard[newc][r] = board[c][r]
            newboard[c][r] = None
            moves.append(newboard)
            if eat:
                break
            newc += k
    for l in [1, -1]:
        newr = r + l
        while newr in range(4):
            if board[c][newr] != None and board[c][newr][1] == board[c][r][1]:
                break
            if board[c][newr] != None and board[c][newr][0] == "Q":
                eatqueen = True
            eat = (board[c][newr] != None)
            newboard = cloneboard(board)
            newboard[c][newr] = board[c][r]
            newboard[c][r] = None
            moves.append(newboard)
            if eat:
                break
            newr += l
    return (moves, eatqueen)


def echecmat(board, m):
    if m < 1:
        return False

    whiteturn = (m % 2 == 1)
    possibilities = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != None and board[i][j][1] == whiteturn:
                (moves, eatqueen) = getmoves(board, i, j)
                if eatqueen:
                    return whiteturn
                possibilities += moves

    for possibility in possibilities:
        if echecmat(possibility, m - 1) == whiteturn:
            return whiteturn
    else:
        return not whiteturn


T = int(input())
for t in range(T):
    (w, b, m) = map(int, input().split(" "))
    board = [[None for j in range(4)] for i in range(4)]
    for i in range(w):
        (t, c, r) = input().split(" ")
        c = ord(c) - ord("A")
        r = int(r) - 1
        board[c][r] = [t, True]
    for i in range(b):
        (t, c, r) = input().split(" ")
        c = ord(c) - ord("A")
        r = int(r) - 1
        board[c][r] = [t, False]

    if m % 2 == 0:
        m -= 1
    result = echecmat(board, m)
    if result:
        print("YES")
    else:
        print("NO")