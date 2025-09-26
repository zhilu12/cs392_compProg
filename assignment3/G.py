from collections import deque
import sys 
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

color = [0] * (n + 1)

def bfs(u):
    q = deque([u])
    color[u] = 1
    while q:
        u = q.popleft()
        for v in adj[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]
                q.append(v)
            elif color[v] == color[u]:
                return False
            
    return True

for i in range(1, n + 1):
    if color[i] == 0 and adj[i]:
        if not bfs(i):
            print(-1)
            sys.exit(0)

a, b = [], []
for i in range(1, n + 1):
    if color[i] == 1:
        a.append(i)
    elif color[i] == 2:
        b.append(i)

print(len(a))
print(" ".join(map(str, a)))
print(len(b))
print(" ".join(map(str, b)))