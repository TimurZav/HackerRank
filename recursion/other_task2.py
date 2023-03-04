import re


# def decode(s: str) -> str:
#
#     return decode(re.sub(r"(\d+)\[([a-z]+)]", lambda m: m[2] * int(m[1]), s)) if "[" in s else s
#
#
# print(decode("ab2[c2[de]11[f]]eh"))


def decode(s: str) -> str:
    if "[" in s:
        # x = re.findall(r"(\d+)\[([a-z]+)]", s)
        # z = lambda m: m[0][1] * int(m[0][0])
        # print(z(x))
        return decode(re.sub(r"(\d+)\[([a-z]+)]", lambda m: m[2] * int(m[1]), s))
    else:
        return s


print(decode("ab2[c2[de]11[f]]eh"))
