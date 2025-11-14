from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
hash = defaultdict(int)
distinct = 0
res = 0

for r in range(n):
    if hash[arr[r]] == 0:
        distinct += 1
    hash[arr[r]] += 1

    while distinct > k:
        hash[arr[l]] -= 1
        if hash[arr[l]] == 0:
            distinct -= 1
        l += 1

    res += (r - l) + 1

print(res)
