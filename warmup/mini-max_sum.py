a = input().strip().split(' ')
for i in range(len(a)):
    a[i] = int(a[i])

s = sum(a)
print(f"{str(s - max(a))} {str(s - min(a))}")