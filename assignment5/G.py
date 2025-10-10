class DSU:
    def __init__(self,n):
        n=n+1
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]
        self.components = n - 1

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        if self.size[x] > self.size[y]:
            x,y = y,x 
        self.parent[x]=y
        self.size[y] += self.size[x]
        self.components -= 1
        return True
    
    def connected(self):
        return self.components == 1

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    d = DSU(n)

    lowerK = []
    greaterK = []

    maxSpeedLowerK = None
    minSpeedGreaterK = None

    for _ in range(m):
        x, y, s = map(int, input().split())
        e = (x,y,s)
        if s <= k:
            lowerK.append(e)
            if maxSpeedLowerK is None or s > maxSpeedLowerK:
                maxSpeedLowerK = s
        else:
            greaterK.append(e)
            if minSpeedGreaterK is None or s < minSpeedGreaterK:
                minSpeedGreaterK = s

    for e in lowerK:
        x, y, s = e
        d.union(x, y)

    if d.connected():
        incCost = (k - maxSpeedLowerK) if maxSpeedLowerK is not None else float('inf')
        decCost = (minSpeedGreaterK - k) if minSpeedGreaterK is not None else float('inf')

        res = min(incCost, decCost)
        print(0 if res == float('inf') else res)
    else:
        greaterK.sort(key=lambda edge: edge[2])
        cost = 0

        for x, y, s in greaterK:
            if d.union(x, y):
                cost += (s - k)
                if d.connected():
                    break

        print(cost)
    