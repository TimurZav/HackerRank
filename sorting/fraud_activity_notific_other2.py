from bisect import bisect_left, insort_left

n, d = map(int, input().split())
list_full = list(map(int, input().split()))
notification = 0
list_range = sorted(list_full[:d])


def get_median():
    return list_range[d//2] if d % 2 == 1 else ((list_range[d//2] + list_range[d//2-1]) / 2)


for i in range(d, n):
    if list_full[i] >= 2 * get_median():
        notification += 1
    del list_range[bisect_left(list_range, list_full[i-d])]
    insort_left(list_range, list_full[i])
print(notification)
