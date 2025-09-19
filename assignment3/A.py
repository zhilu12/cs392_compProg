from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
visited = [False] * (n+1)
parents = [0] * (n+1) 

for _ in range(m):
  a, b = map(int, input().split())
  
  adj[a].append(b)
  adj[b].append(a)

team1 = set()
team2 = set()

q = deque()

"""
BFS starting from the first node, mark as visited when seen?


"""

for i in range(n):
  # check for friends
  if not visited[n]:
    bfs
    