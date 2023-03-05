def decode_like_normal_man(sentence):
    k = 0
    boxes = [[1, '']]
    for x in sentence:
        if 47 < ord(x) < 58:
            k = k*10+int(x)
        elif x == '[':
            boxes.append([k, ''])
            k = 0
        elif x == ']':
            multi, res = boxes.pop(-1)
            boxes[-1][1] += multi*res
        else:
            boxes[-1][1] += x
    return boxes[0][0]*boxes[0][1]


print(decode_like_normal_man('ab2[b2[cd]10[e]]f'))


def decode(sentence, f=None):
    k = 0
    res = ''
    if f is None:
        f = 0
    while f < len(sentence):
        now = sentence[f]
        if 47 < ord(now) < 58:
            k = k*10 + int(now)
        elif now == '[':
            answer, f = decode(sentence, f+1)
            res += k*answer
            k = 0
        elif now == ']':
            return res, f
        else:
            res += now
        f += 1
    return res


print(decode('ab2[b2[cd]]f'))  # --> abbcdcdeeeeeeeeeebcdcdeeeeeeeeeef

