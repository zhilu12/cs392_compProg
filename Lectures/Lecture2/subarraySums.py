n, x = map(int, input().split())

arr = list(map(int, input().split()))

l, r = 0,0
sum = 0
res = 0

for r in range(n):
  sum += arr[r]
  
  while sum > x:
    sum -= arr[l]
    l += 1
    
  if sum == x:
    res += 1
    
  
print(res)