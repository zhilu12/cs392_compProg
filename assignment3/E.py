n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    rev[v].append(u)

visited = [False] * (n + 1)
order = []

def dfs1(u):
    stack = [(u, 0)]
    visited[u] = True
    while stack:
        u, st = stack[-1]
        if st < len(adj[u]):
            v = adj[u][st]
            stack[-1] = (u, st + 1)
            if not visited[v]:
                visited[v] = True
                stack.append((v, 0))
        else:
            order.append(u)
            stack.pop()

for i in range(1, n + 1):
    if not visited[i]:
        dfs1(i)

kingdom = [0] * (n + 1)
k = 0

def dfs2(u, label):
    kingdom[u] = label
    
    stack = [u]
    while stack:
        u = stack.pop()
        for v in rev[u]:
            if kingdom[v] == 0:
                kingdom[v] = label
                stack.append(v)

for u in reversed(order):
    if kingdom[u] == 0:
        k += 1
        dfs2(u, k)

print(k)
print(" ".join(str(kingdom[i]) for i in range(1, n + 1)))