info =[0]*3
info = list(map(int, input().split()))
com = [0]*info[1]
dfs_graph = {}
bfs_graph= {}

def bfs(graph, node):
    visit=[]
    queue =[]

    queue.append(node)
    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
    return " ".join(map(str,visit))

def dfs(graph, node):

    visit=[]
    stack =[]

    stack.append(node)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return " ".join(map(str,visit))

def bfs_sort(val,i):
    val.sort(reverse=False)  
    bfs_graph[i] = val
    

def dfs_sort(d_val,i):  
    
    d_val.sort(reverse=True) 
    dfs_graph[i]=d_val



for i in range(info[1]):
    com[i]=list(map(int, input().split()))

for i in range(1, info[0]+1):
    val=[]
    for list in com:
        if i in list:
            if list[0] == i:
                val.append(list[1])
            else :
                val.append(list[0])
    d_val = val.copy()
    dfs_sort(d_val,i)         
    bfs_sort(val,i)
    
    
print(dfs(dfs_graph, info[2]))
print(bfs(bfs_graph, info[2]))
