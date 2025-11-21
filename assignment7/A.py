n = int(input())

r = n * n
l = 1
goal = (n * n) // 2 + 1

def count(x):
    res = 0
    for i in range(1, n + 1):
        # x//i is number of multiples that goes into x of i
        res += min(n, x // i)
    return res

while l < r :
    m = (l + r) // 2

    test = count(m)
    if test >= goal:
        r = m
    else:
        l = m + 1

print(l)