n = int(input())
m = int(input())

from collections import defaultdict
Dict = defaultdict(list)

visited = [False]*(n+1)

for _ in range(m):
  start, end = map(int, input().split())

  Dict[start].append(end)
  Dict[end].append(start)

def dfs(graph, i, visited):
  visited[i] = True
  # print(i, end=' ')
  for j in graph[i]:
    if not visited[j]:
      dfs(graph, j, visited)

dfs(Dict, 1, visited)

print(visited.count(True)-1)