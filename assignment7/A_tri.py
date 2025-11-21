n = int(input())

# for 5: 5 * 6 / 2 = 15 -> 8th value
s = (n * (n+1) // 2) // 2 + 1

# num of values up to a
def cal(a):
    return (a * (a+1) // 2)

row = -1
l = 1
r = n

while l <= r:
    m = (l + r) // 2

    if cal(m-1) < s <= cal(m):
        row = m
        break
    elif cal(m) <  s:
        l = m + 1
    else:
        r = m - 1

prev = cal(row - 1)

print(row * (s-prev))