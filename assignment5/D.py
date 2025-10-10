class DSU:
    def __init__(self,n):
        self.parent = list(range(n + 2))


    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    def full(self, x):
        self.parent[x] = self.find(x + 1)
            
        
n = int(input())
cap = [0] + list(map(int, input().split()))
vol = [0] * (n + 1)
m = int(input())
d = DSU(n)

for _ in range(m):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # p_i, x_i: p_i vessel, x_i liters of water
        p, x = query[1], query[2]
        i = d.find(p)

        while x > 0 and i <= n:
            aval = cap[i] - vol[i]
            if aval > 0:
                temp = min(x, aval)
                x -= temp
                vol[i] += temp

                if vol[i] == cap[i]:
                    d.full(i)

            else:
                d.full(i)
            i = d.find(i)


    else:
        k = query[1]
        print(vol[k])

