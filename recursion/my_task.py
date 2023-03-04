import re

string = "2[a2[b2[c1[vv]]]]3[x4[z]]8[k]1[n]2[r]"
# string = "3[a]2[bc]"


def get_last_nested(match, nested_brackets, last_nested):
    match2 = f"{match}]"
    for brackets in nested_brackets:
        if match2 == brackets:
            last_nested.append(brackets)


def get_all_nested(list_matches, nested_brackets, all_nested):
    i = 0
    is_consecutive_entry = False
    for index, nested_match in enumerate(list_matches):
        nested_match = f"{nested_match}]"
        if nested_match == nested_brackets[i]:
            if is_consecutive_entry:
                is_consecutive_entry = False
                print("consecutive entry")
                all_nested.append(nested_match)
                all_nested.append("")
            i += 1
        else:
            is_consecutive_entry = True
            all_nested.append(nested_match)


def main(string_test):
    test = ""
    last_nested = []
    all_nested = []
    list_matches = re.findall(r"\d+\[[a-z]+", string_test)
    nested_brackets = re.findall(r"\d+\[[a-z]+\]", string_test)
    for match in list_matches:
        get_last_nested(match, nested_brackets, last_nested)
        get_all_nested(list_matches, nested_brackets, all_nested)
        matches = match.split("[")
        test += matches[1] * int(matches[0])
    print(test)
    print(last_nested)


main(string)
