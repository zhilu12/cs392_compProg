n = int(input())
arr = list(map(int, input().split()))

cnt = [0] * n
cnt[0] = 1

res = pref = 0

for num in arr:
    pref += num
    pref %= n

    res += cnt[pref]
    cnt[pref] += 1

print(res)