n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
m = len(arr)//2

def possible(mid):
    need = 0

    for i in range(m, n):
        if arr[i] < mid:
            need += (mid - arr[i])
            if need > k:
                return False
    return need <= k

l, r = arr[m], arr[m] + k

while l < r:
    mid = (l + r + 1) // 2
    if possible(mid):
        l = mid
    else:
        r = mid - 1

print(l)