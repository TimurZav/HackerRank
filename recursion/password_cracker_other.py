test_case: int = 1


def solve(list_passwords, login):
    dead_end = set()
    stack = [([], login)]
    while stack:
        acc, cur = stack.pop()
        if cur == "":
            return acc
        is_dead_end = True
        for password in list_passwords:
            if cur.startswith(password):
                cur2 = cur[len(password):]
                if cur2 in dead_end:
                    continue
                is_dead_end = False
                acc2 = acc[:]
                acc2.append(password)
                stack.append((acc2, cur2))

        if is_dead_end:
            dead_end.add(cur)


for _ in range(test_case):
    count_space_separated: int = 6
    passwords: list = "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa".split()
    login_attempt: str = "aaaaaaaaaab"
    answer = solve(passwords, login_attempt)
    if answer is None:
        print("WRONG PASSWORD")
    else:
        print(" ".join(answer))
