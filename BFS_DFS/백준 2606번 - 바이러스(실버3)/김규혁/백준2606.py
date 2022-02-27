import sys

sys.stdin = open('input.txt', 'r')

computer = int(input())
net = int(input())

graph = [[]*computer for _ in range(computer+1)]

for _ in range(net):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(computer+1)

def dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)