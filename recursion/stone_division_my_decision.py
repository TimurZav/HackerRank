

def count_pile():
    global index_global
    index_global += 1


def stone_division(n, s, main):
    if not n:
        return
    for pile in n:
        for divider in sorted(s, reverse=True):
            if pile % divider == 0 and pile != divider:
                piece = pile // divider
                pile = divider
                list_pile = [pile for _ in range(piece)]
                stone_division(list_pile, s, main)
                count_pile()
                break


if __name__ == '__main__':
    q = 2
    for _ in range(q):
        n = 377083280820
        m = 10
        s = [1, 377083280820, 2, 188541640410, 3, 125694426940, 4, 94270820205, 5, 75416656164]
        index_global = 0
        stone_division([n], s, n)
        print(index_global)
