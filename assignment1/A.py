n = int(input())

res = []

while n != 1:
    res.append(str(int(n)))
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1

res.append("1")

print(" ".join(res))