from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  
  adj[a].append(b)
  adj[b].append(a)

team = [0] * (n + 1)

def bfs(u):
  q = deque()
  team[u] = 1
  for v in adj[u]:
    if team[v] == 0:
      team[v] = 3 - team[u]
      q.append(v)
    elif team[v] == team[u]:
      return False

  return True

possible = True
for i in range(1, n + 1):
  if team[i] == 0:
    if not bfs(i):
      possible = False
      break
  
if possible:
  print(" ".join(str(team[i]) for i in range(1, n + 1)))
else:
  print("IMPOSSIBLE")