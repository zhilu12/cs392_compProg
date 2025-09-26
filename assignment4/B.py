n = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

l, r = min(arr1), max(arr2)
slowest = min(arr2)

while l <= r:
  m = (l + r) // 2
  
  lowerB = max([abs(x - l) for x in arr1]/arr2)
  
  upperB = max([abs(x - r) for x in arr1]/arr2)
  
  diff = max([abs(x - m) for x in arr1/arr2])
  
  if lowerB < upperB and lowerB < diff:
    r = m
  else:
    l = m
  
  
  
# x - 