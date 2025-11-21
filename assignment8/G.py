n, x = map(int, input().split())
coins = list(map(int, input().split()))

INF = 10**9
dp = [INF] * (x + 1)

dp[0] = 0

for c in coins:
    d = dp
    for s in range(c, x + 1):
        prev = d[s-c] + 1
        if prev < d[s]:
            d[s] = prev

print(-1 if dp[x] > x else dp[x])