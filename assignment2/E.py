t = int(input())

while t > 0:
    n = int(input())
    s = str(input())

    l, r = 0, n - 1

    res = n
    while l < r:
        if (s[l] == '0' and s[r] == '1') or (s[l] == '1' and s[r] == '0'):
            l += 1
            r -= 1
            res -= 2
        else:
            break

    t -= 1
    print(res)
