n = int(input())
arr = list(map(int, input().split()))

sums = [0] * (n + 1)
for i in range(1, n + 1):
    sums[i] = sums[i - 1] + arr[i - 1]

res = 0

for i in range(0, n):
    for j in range(i + 1, n + 1):
        if (sums[j] - sums[i]) % n == 0:
            res += 1

print(res)