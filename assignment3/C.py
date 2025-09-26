from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
rev = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    rev[b].append(a)


def bfs(start, adj):
    n = len(adj) - 1
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    return visited

start = 1
forward = bfs(start, adj)
found = False
for v in range(1, n + 1):
    if not forward[v]:
        print("NO")
        print(start, v)
        found = True
        break
    
if not found:
    backward = bfs(start, rev)
    for v in range(1, n+1):
        if not backward[v]:
            print("NO")
            print(v, start)
            found = True
            break

if not found:
    print("YES")