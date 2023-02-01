# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

sys.setrecursionlimit(150000)

T = int(input())


def find_password2(password, passdb, mem):
    if mem.has_key(password):
        return mem[password]
    for i in range(min(11, len(password) + 1)):
        p = password[:i]
        if p in passdb:
            r = password[i:]
            if len(r) == 0:
                mem[password] = p
                return p
            else:
                w = find_password2(password[i:], passdb, mem)
                if not w is None:
                    res = p + " " + w
                    mem[password] = res
                    return res
    mem[password] = None
    return None


for _ in range(T):
    n = int(input())
    passwd = input().strip().split()
    a = input().strip()
    mem = {}

    passwd.sort(key=lambda x: len(x))

    p = find_password2(a, passwd, mem)

    if not p is None:
        print(p)
    else:
        print("WRONG PASSWORD")