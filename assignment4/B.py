n = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

l = 0
r = (max(arr1) - min(arr1))/min(arr2)

for _ in range(60):
  m = (l + r) / 2
  back = max(arr1[i] - arr2[i]*m for i in range(n))
  forward = min(arr1[i] + arr2[i]*m for i in range(n))

  if back <= forward:
    r = m
  else:
    l = m

print(l)