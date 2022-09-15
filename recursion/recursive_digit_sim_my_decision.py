

def superDigit(digits, k):
    if len(digits) == 1:
        return digits
    digit = sum(int(digit) for digit in digits) * k
    return superDigit(str(digit), 1)


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()
    # n = first_multiple_input[0]
    # k = int(first_multiple_input[1])

    n = "148"
    k = 3
    print(superDigit(n, k))
