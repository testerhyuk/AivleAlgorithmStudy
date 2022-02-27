#https://www.acmicpc.net/problem/1260

node, i, start = map(int, input().split())
graph = [[] for _ in range(node + 1)]
visited = [False for _ in range(node+1)]
queue = [start]

for _ in range(i):
    [s, e] = map(int, input().split(" "))
    graph[s].append(e)
    graph[e].append(s)

for x in range(0, node+1):
    if graph[x]:
        graph[x].sort()


def DFS(x):
    visited[x] = True
    print(x, end = " ")

    for go in graph[x]:
        if(not visited[go]):
            DFS(go)

def BFS(x):
    while(len(queue)):
        n = queue.pop(0)
        print(n, end = " ")
        for go in graph[n]:
            if(not visited[go]):
                queue.append(go)
                visited[go] = True


                

DFS(start)
print("")
#초기화
visited = [False for _ in range(node+1)]
visited[start] = True
BFS(start)