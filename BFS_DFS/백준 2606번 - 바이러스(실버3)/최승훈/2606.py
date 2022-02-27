#https://www.acmicpc.net/problem/2606

node = int(input())
i = int(input())
graph = [[] for _ in range(node + 1)]
visited = [False for _ in range(node + 1)]

#0번 제외
visited[0] = True

for _ in range(i):
    [s, e] = map(int, input().split(" "))
    graph[s].append(e)
    graph[e].append(s)


#BFS


#시작점
queue = [1]
visited[1] = True

def bfs():
    while(len(queue)):
        #shift
        n = queue.pop(0)
        for go in graph[n]:
            if(not visited[go]):
                queue.append(go)
                visited[go] = True

bfs()
#0, 시작점 제외
print(visited.count(True) -2)
