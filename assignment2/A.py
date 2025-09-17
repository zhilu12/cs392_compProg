from collections import deque
import heapq

n, k = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()
h = []
heapq.heapify(h)

res = []
r = 0
l = 0

while r < n:
    while r - l + 1 < k:
        heapq.heappush(h, arr[r])
        r += 1
    res.append(h[k//2])
    
        
    

  
  
print(*res)