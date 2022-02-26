n, m, v = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

def show(matrix):
  print()
  for i in matrix:
    for j in i:
      print(j, end=' ')
    print()

for _ in range(m):
  f, t = map(int, input().split())
  if graph[f] == []:
    graph[f] = [t]
  else:
    graph[f].append(t)
  if graph[t] == []:
    graph[t] = [f]
  else:
    graph[t].append(f)

for i in graph:
  i.sort()
def dfs(graph, i, visited):
  visited[i] = True
  print(i, end=' ')
  for j in graph[i]:
    if not visited[j]:
      dfs(graph, j, visited)

stack = []
def dfs_stack(graph, i, visited):
  stack = [i]
  visited[i] == True
  while stack:
    value = stack.pop()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
    for j in graph[value]:
      if not visited[j]:
        stack.append(j)


    # print(stack)
# print(graph)

for i in graph:
  i.reverse()
import time

start = time.time()
visited = [False] * (n+1)
dfs_stack(graph, v, visited)
end = time.time()
print(end-start)

from collections import deque

# print(graph)
def bfs(graph, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()

    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for j in graph[value]:
        queue.append(j)

dfs(graph, v, visited)
visited = [False] * (n+1)
print()
bfs(graph, v, visited)