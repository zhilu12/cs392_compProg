n, k = map(int, input().split())
arr = list(map(int, input().split()))

def feasible(arr, mid, k):
    sub = 1
    sum = 0
    for num in arr:
        if sum + num <= mid:
            sum += num
        else:
            sub += 1
            sum = num
            if sub > k:
                return False
    return True

l, r = max(arr), sum(arr)

while l < r:
    mid = (l + r) // 2

    if feasible(arr, mid, k):
        r = mid
    else:
        l = mid + 1

print(l)