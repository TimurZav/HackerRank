def indi(L, num):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if L[mid] == num:
            return mid
        elif L[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def insertIndi(L, num):
    if len(L) == 0: return 0
    if L[0] >= num: return 0
    if L[len(L) - 1] <= num: return len(L)

    low = 0
    high = len(L) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if L[mid] >= num >= L[mid - 1]: return mid
        if L[mid] > num:
            high = mid - 1
        else:
            low = mid + 1


def main():
    n, d = map(int, input().split())
    A = list(map(int, input().split()))
    L = A[:d]
    L.sort()
    ans = 0
    rmv = 0
    i = d
    while i < n:
        # print L
        mid = d // 2
        if d % 2 == 0:
            if (L[mid] + L[mid - 1]) % 2 == 0:
                median = (L[mid] + L[mid - 1]) // 2
            else:
                median = (L[mid] + L[mid - 1]) / 2.0
        else:
            median = L[mid]
        index = indi(L, A[rmv])
        # print index, A[rmv]
        L.pop(index)
        index = insertIndi(L, A[i])
        L.insert(index, A[i])
        if median * 2 <= A[i]:
            ans += 1
        rmv += 1
        i += 1
    print(ans)


main()