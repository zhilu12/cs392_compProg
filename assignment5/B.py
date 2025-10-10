from collections import deque

class DSU:
    def __init__(self,n):
        n=n+1
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.size[x] < self.size[y]:
                x,y = y,x 

            seq[x].extend(seq[y]) 
            seq[y].clear()  

            self.parent[y] = x
            self.size[x] += self.size[y]
            

n = int(input())
d = DSU(n)
seq = [deque([i]) for i in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    d.union(a, b)

root = d.find(1)
print(" ".join(map(str, seq[root])))
