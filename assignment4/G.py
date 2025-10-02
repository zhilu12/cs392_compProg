n, k = map(int, input().split())
req = list(map(int, input().split()))
num = list(map(int, input().split()))

l, r = 0, (max(num) + k)//min(req)

def feasible(m):
    need = 0

    for i in range(n):
        if m > num[i]//req[i]:
            need += (m * req[i] - num[i])
            if need > k:
                return False
            
    return True

while l < r:
    mid = (l + r + 1)//2

    if feasible(mid):
        l = mid
    else:
        r = mid - 1

print(l)