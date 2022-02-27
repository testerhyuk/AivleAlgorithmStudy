import sys
from collections import deque

sys.stdin = open('input.txt', 'r')

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

visited = [False] * (n + 1)

# DFS
def dfs(v):
    visited[v] = True

    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# BFS
def bfs(v):
    q=deque([v])
    visited[v]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i]=True

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)