n, k = map(int, input().split())
arr = list(map(int, input().split()))

l = 0
r = 0

res = []

# l = 0, r = k
while r < n - 1 and l < n - k:
  while r - 1 < k:
    r += 1
  res.append(sorted(arr[l:r])[k // 2])
  l += 1
  

  
  
print(*res)