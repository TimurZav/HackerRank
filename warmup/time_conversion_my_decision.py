import re


def timeConversion(s):
    digits = re.findall("\d{1,2}", s)
    if 'PM' in s:
        six_hour = 24 - 6
        hours = six_hour + int(digits[0])
        hours = hours - 24
        hours = str(six_hour + hours) if int(digits[0]) != 12 else str(six_hour - hours)
    else:
        hours = 12 - (12 - int(digits[0]))
        hours = f"0{str(hours)}" if hours < 10 else f"0{str(12 - hours)}"
    return f"{hours}:{str(digits[1])}:{str(digits[2])}"


if __name__ == '__main__':
    # s = '12:40:22AM'
    s = '12:45:54PM'
    result = timeConversion(s)
    print(result)


