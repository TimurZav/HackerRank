from statistics import median


def activity_notifications(expenditure, d):
    count_notification = 0
    for i in range(d-1):
        median_in_list = median(expenditure[i:d+i])
        try:
            next_elem = expenditure[d + i:d + i + 1][0]
        except IndexError:
            continue
        if median_in_list * 2 <= next_elem:
            count_notification += 1
    return count_notification


if __name__ == '__main__':
    n = 9
    d = 5
    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    count = 0
    for i in range(d):
        expenditure_range = expenditure[i % n:d + i]
        if next_elem := expenditure[d + i:d + i + 1]:
            if median(expenditure_range) * 2 <= next_elem[0]:
                count += 1
    print(count)

    # first_multiple_input = input().rstrip().split()
    # n = int(first_multiple_input[0])
    # d = int(first_multiple_input[1])
    # expenditure = list(map(int, input().rstrip().split()))
    # print(activity_notifications(expenditure, d))
