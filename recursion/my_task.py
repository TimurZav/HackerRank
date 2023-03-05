# import re
#
# string = "ab2[b2[cd]]f"
# # string = "3[a]2[bc]"
#
#
# def get_last_nested(match, nested_brackets, last_nested):
#     match2 = f"{match}]"
#     for brackets in nested_brackets:
#         if match2 == brackets:
#             last_nested.append(brackets)
#
#
# def get_all_nested(list_matches, nested_brackets, all_nested):
#     i = 0
#     is_consecutive_entry = False
#     for nested_match in list_matches:
#         nested_match = f"{nested_match}]"
#         if nested_match == nested_brackets[i]:
#             if is_consecutive_entry:
#                 is_consecutive_entry = False
#                 all_nested.append(nested_match)
#                 all_nested.append("")
#             i += 1
#         else:
#             is_consecutive_entry = True
#             all_nested.append(nested_match)
#
#
# def main(string_test):
#     test = ""
#     last_nested = []
#     all_nested = []
#     list_matches = re.findall(r"\d+\[[a-z]+", string_test)
#     nested_brackets = re.findall(r"\d+\[[a-z]+\]", string_test)
#     get_all_nested(list_matches, nested_brackets, all_nested)
#     for match in list_matches:
#         get_last_nested(match, nested_brackets, last_nested)
#         matches = match.split("[")
#         test += matches[1] * int(matches[0])
#     print(test)
#     print(all_nested)
#
#     lst = ['2[b]', '2[cd]', '']
#     result_str = ''
#     for s in lst:
#         match = re.match(r'^(\d*)\[(\w+)\]$', s)
#         if match:
#             count = int(match.group(1)) if match.group(1) else 1
#             sub_str = match.group(2)
#             result_str += (sub_str * count)
#
#     print(result_str)
#
#
# main(string)


def decode_string(s):
    stack = []
    curr_str = ""
    curr_num = 0

    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == "[":
            stack.append(curr_str)
            stack.append(curr_num)
            curr_str = ""
            curr_num = 0
        elif c == "]":
            num = stack.pop()
            prev_str = stack.pop()
            curr_str = prev_str + curr_str * num
        else:
            curr_str += c

    return curr_str


print(decode_string("ab2[b2[cd]10[e]]f"))
