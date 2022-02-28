info =[0]*2
info = list(map(int, input().split()))
root = []

for i in range(info[0]):
    root.append(list(map(int, input())))

def bfs(node):

    visit=[]
    queue =[]
    cnt = {}
    cnt[0,0] = 1


    queue.append(node)
    while queue:
        node = queue.pop(0)
        
        #아직 가지 않은 길일경우 경로에 추가하고 상하좌우에 다음 길이 있는지 확인하여
        #그 길의 누적 길이를 저장한다. -> cnt[0,0] = 1 : 0,0은 길의 누적 길이 1
        if node not in visit:
            visit.append(node)
            
            #우
            #try는 over list 되는것을 방지
            try:
                if root[node[0]][node[1]+1]==1:
                    queue.append([node[0],node[1]+1])
                    #상하좌우 탐색 시 똑같은 길이 중복될 경우를 제거
                    if (node[0], node[1]+1) not in cnt:  
                        cnt[node[0], node[1]+1] = cnt[node[0], node[1]]+1
            except:
                pass
            
            #하
            try:
                if root[node[0]+1][node[1]]==1:
                    queue.append([node[0]+1,node[1]])
                    if (node[0]+1, node[1]) not in cnt:  
                        cnt[node[0]+1, node[1]] = cnt[node[0], node[1]]+1
            except:
                pass       
            
            #좌
            if root[node[0]][node[1]-1]==1:
                #list값이 음수가 되는것을 방지
                if node[1]-1>=0:
                    queue.append([node[0],node[1]-1])
                    if (node[0], node[1]-1) not in cnt:  
                            cnt[node[0], node[1]-1] = cnt[node[0], node[1]]+1

            #상
            if root[node[0]-1][node[1]]==1:
                if node[0]-1>=0:
                    queue.append([node[0]-1,node[1]])
                    if (node[0]-1, node[1]) not in cnt:  
                            cnt[node[0]-1, node[1]] = cnt[node[0], node[1]]+1



    #출구의 누적 길의 길이를 출력    
    return print(cnt[[info]-1, info[1]-1])

bfs([0,0])
