import sys

sys.setrecursionlimit(5000)


def hack(att):
    if att == '': return ''
    legit = [l for l in pwds if l == att[:len(l)]]
    if not legit: return False
    for l in legit:
        if att[len(l):] in seen: continue
        n = hack(att[len(l):])
        if n != False:
            return l + ' ' + n
        else:
            seen.add(att[len(l):])
    return False


for _ in range(int(input())):
    seen = set()
    n = int(input())
    pwds = input().split()
    att = input()
    h = hack(att)
    print(h if h else 'WRONG PASSWORD')