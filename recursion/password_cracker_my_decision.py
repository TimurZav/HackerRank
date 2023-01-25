import re


def password_cracker(list_password: list, login: str) -> str:
    list_iter: list = []
    is_wrong_password = False
    is_check_password = False
    login_copy = login
    count_duplicate = 0
    not_count_duplicate = 0
    x = 0
    for password in list_password:
        if not re.findall(password, login):
            for right_password in list_password:
                if right_password in login:
                    is_wrong_password = False
                    is_check_password = True
                    x += 1
            if not is_check_password or x < 2:
                is_wrong_password = True
        elif re.findall(password, login_copy):
            login_copy = login_copy.replace(re.findall(password, login)[0], "", 1)
            count_duplicate += 1
        else:
            not_count_duplicate += 1
        list_iter.extend(tuple_match_iter.span()[1] - 1 for tuple_match_iter in re.finditer(password, login))
    list_iter.sort(reverse=True)
    for index_space in list_iter:
        login: str = f'{login[:index_space + 1]} {login[index_space + 1:]}'
    return "WRONG PASSWORD" if is_wrong_password or (not_count_duplicate > 0 and login_copy != '') else login.strip()


if __name__ == '__main__':
    test_case: int = 1
    for _ in range(test_case):
        count_space_separated: int = 6
        passwords: list = "ylphk zzfkifd esfsnbkp ftszfcqp simdoclmcl rwya hmfndblkd waapaw ybyikf yuhhrev".split()
        login_attempt: str = "yuhhrevyuhhrefylphzwaapawstszfcqpyuhhrevybyikfybyikfyuhhyevybyykgbsfsnykp"
        result = password_cracker(passwords, login_attempt)
        print(result)

