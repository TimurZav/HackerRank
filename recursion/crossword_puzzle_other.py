# write your code here
def isStart(availwords, s):
    for i in availwords:
        if i[0] == s:
            return True
    return False


def checkhorizontal(grid, curword, r, c):
    for i in range(len(curword)):
        if c + i >= 10:
            return False
        if grid[r][c + i] == "-" or grid[r][c + i] == curword[i]:
            pass
        else:
            return False
    return True


def sethorizontal(grid, curword, r, c, b):
    for i in range(len(curword)):
        if grid[r][c + i] == "-":
            grid[r][c + i] = curword[i]
        else:
            b[i] = False


def resethorizontal(grid, curword, r, c, b):
    for i in range(len(curword)):
        if b[i] == True:
            grid[r][c + i] = "-"


def checkvertical(grid, curword, r, c):
    for i in range(len(curword)):
        if r + i >= 10:
            return False
        if grid[r + i][c] == "-" or grid[r + i][c] == curword[i]:
            pass
        else:
            return False
    return True


def setvertical(grid, curword, r, c, b):
    for i in range(len(curword)):
        if grid[r + i][c] == "-":
            grid[r + i][c] = curword[i]
        else:
            b[i] = False


def resetvertical(grid, curword, r, c, b):
    for i in range(len(curword)):
        if (b[i] == True):
            grid[r + i][c] = "-"


def crossword(grid, words, index):
    if index == len(words):
        for r in range(10):
            for c in grid[r]:
                print(c, end="")
            print()
        return True

    curword = words[index]
    for r in range(10):
        for c in range(10):
            if grid[r][c] == "-" or grid[r][c] == curword[0]:
                if checkhorizontal(grid, curword, r, c):
                    b = [True] * len(curword)
                    sethorizontal(grid, curword, r, c, b)
                    if crossword(grid, words, index + 1):
                        return True
                    else:
                        resethorizontal(grid, curword, r, c, b)
                if checkvertical(grid, curword, r, c):
                    b1 = [True] * len(curword)
                    setvertical(grid, curword, r, c, b1)
                    if crossword(grid, words, index + 1):
                        return True
                    else:
                        resetvertical(grid, curword, r, c, b1)


grid = []
for _ in range(10):
    r = input()
    r1 = list(r)
    grid.append(r1)
words = list(input().split(";"))
crossword(grid, words, 0)

