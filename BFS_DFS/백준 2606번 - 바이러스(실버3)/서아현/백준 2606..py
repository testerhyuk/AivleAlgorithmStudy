num = int(input())
connect = int(input())
com = [0]*connect
val2=[]
computer = {}

for i in range(connect):
    com[i]=list(map(int, input().split()))

for i in range(1, num+1):
    val=[]
    for list in com:
        if i in list:
            if list[0] == i:
                val.append(list[1])
            else :
                val.append(list[0])
    val2.append({
        i:val
    })

    computer[i] = set(val2[i-1][i])

def bfs(graph, node):
    visit=[]
    queue =[]

    queue.append(node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return len(visit)-1

print(bfs(computer, 1))
