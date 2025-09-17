n = int(input())

arr = list(map(int, input().split()))

hash = {}
l = 0

res = 0

for r in range(n):
  if arr[r] in hash:
    l = max(hash[arr[r]] + 1, l)
    
  hash[arr[r]] = r
  
  res = max(res, r - l + 1)
  
print(res)
    
    