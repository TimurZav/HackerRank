
def decode(inp: str, s=0):
    r = ''
    k = ''

    while s < len(inp):
        if inp[s] == ']':
            return r, s
        elif inp[s].isnumeric():
            k += inp[s]
        elif inp[s] == '[':
            decode_res = decode(inp, s + 1)
            r += decode_res[0] * int(k)
            k = ''
            s = decode_res[1]
        else:
            r += inp[s]
        s += 1
    return r


assert decode('3[a]') == 'aaa'
assert decode('3[a]2[bc]') == 'aaabcbc'
assert decode('2[a2[b]]') == 'abbabb'
assert decode('ab2[b2[cd]10[e]]f') == 'abbcdcdeeeeeeeeeebcdcdeeeeeeeeeef'
