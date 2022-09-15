
def display():
    for i in range(10):
        print(grid[i])


def is_valid(text, k):
    i, j, l, x, y = init[k]
    if l != len(text):
        return False
    for t in range(l):
        if grid[i + x*t][j + y*t] not in [ord('-'), ord(text[t])]:
            return False

    return True


def put(text, k):
    i, j, l, x, y = init[k]

    changes = []
    for t in range(l):
        if grid[i + x*t][j + y*t] == ord('-'):
            grid[i + x*t][j + y*t] = ord(text[t])
            changes.append((i + x*t, j + y*t))

    return changes


def revert(changes):
    for i, j in changes:
        grid[i][j] = ord('-')


def Solve(t=0):
    global solved
    if t == len(init) or solved:
        solved = True
        return
    for i in range(len(init)):
        for key in keys:
            if solved: return
            if key not in used and is_valid(key, i):

                used.add(key)
                c = put(key, i)
                Solve(t+1)
                if solved: return
                revert(c)
                used.discard(key)


grid = [bytearray(input(), encoding='utf8') for i in range(10)]
keys = input().split(';')
init = []

for i in range(10):
    for j in range(10):
        if grid[i][j] == ord('-') and (j == 0 or grid[i][j-1] != ord('-')):
            init.append([i, j, 1, 0, 1])

        elif grid[i][j] == ord('-'):
            init[-1][2] += 1

for j in range(10):
    for i in range(10):
        if grid[i][j] == ord('-') and (i == 0 or grid[i-1][j] != ord('-')):
            init.append([i, j, 1, 1, 0])

        elif grid[i][j] == ord('-'):
            init[-1][2] += 1

solved = False
init = list(filter(lambda x: x[2] != 1, init))
used = set()
Solve()
display()