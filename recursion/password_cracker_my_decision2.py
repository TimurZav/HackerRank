import re


def find_right_words(password, login):
    return [
        tuple_match_iter.span()[1] - 1
        for tuple_match_iter in re.finditer(password, login)
    ]


def get_login_with_space(list_iter, login):
    for index_space in list_iter:
        login: str = f'{login[:index_space + 1]} {login[index_space + 1:]}'
    return login


def password_cracker(passwords, login_attempt, list_iter, is_correct_password):
    if not passwords:
        return
    list_index = find_right_words(passwords[0], login_attempt)
    for index in list_index:
        list_iter.append(index)
        list_iter.sort(reverse=True)
    password_cracker(passwords[1:], login_attempt, list_iter, is_correct_password)
    login = get_login_with_space(list_iter, login_attempt)
    if passwords[0] != login_attempt and passwords[0] not in login_attempt:
        is_correct_password = False
    return login.strip() if is_correct_password else "WRONG PASSWORD"


if __name__ == '__main__':
    test_case: int = 1
    for _ in range(test_case):
        count_space_separated: int = 6
        list_iter = []
        is_correct_password = True
        passwords: list = "hello planet".split()
        login_attempt: str = "helloworld"
        result = password_cracker(passwords, login_attempt, list_iter, is_correct_password)
        print(result)

