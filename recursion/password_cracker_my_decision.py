import re


def password_cracker(list_password: list, login: str) -> str:
    list_iter: list = []
    is_wrong_password = False
    is_check_password = False
    for password in list_password:
        if not re.findall(password, login):
            for right_password in list_password:
                if right_password == login:
                    is_wrong_password = False
                    is_check_password = True
            if not is_check_password:
                is_wrong_password = True
        list_iter.extend(tuple_match_iter.span()[1] - 1 for tuple_match_iter in re.finditer(password, login))
    list_iter.sort(reverse=True)
    for index_space in list_iter:
        login: str = f'{login[:index_space + 1]} {login[index_space + 1:]}'
    return "WRONG PASSWORD" if is_wrong_password else login.strip()


if __name__ == '__main__':
    test_case: int = 1
    for _ in range(test_case):
        count_space_separated: int = 4
        passwords: list = "a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa".split()
        login_attempt: str = "aaaaaaaaaab"
        result = password_cracker(passwords, login_attempt)
        print(result)
