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

        if x == y:
            return False
        if self.size[x] > self.size[y]:
            x,y = y,x 
        self.parent[x]=y
        self.size[y] += self.size[x]
        return True
            

n, m, k = map(int, input().split())
d = DSU(n)
components = n

edges = []
for _ in range(m):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    edges.append((a-1, b-1))

broken = []
brokenSet = set()
for _ in range(k):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    e = (a-1, b-1)
    broken.append(e)
    brokenSet.add(e)

for a, b in edges:
    if (a, b) not in brokenSet:
        if d.union(a, b):
            components -= 1

res = [0] * k
for i in range(k - 1, -1, -1):
    res[i] = components
    a, b = broken[i]
    if (d.union(a, b)):
        components -= 1

print(" ".join(map(str, res)))