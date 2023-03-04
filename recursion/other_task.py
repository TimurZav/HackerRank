def decodeString(s):
    stack = []
    curNum = 0
    curString = ''
    for c in s:
        if c == '[':
            stack.append(curString)
            stack.append(curNum)
            curString = ''
            curNum = 0
        elif c == ']':
            num = stack.pop()
            prevString = stack.pop()
            curString = prevString + num * curString
        elif c.isdigit():
            curNum = curNum * 10 + int(c)
        else:
            curString += c
    return curString


x = decodeString("2[a2[b2[c1[vv]]]]3[x4[z]]8[k]1[n]2[r]")
print(x)
