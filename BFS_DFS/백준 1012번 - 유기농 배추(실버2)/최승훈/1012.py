#https://www.acmicpc.net/problem/1012

sticks = []

ux = [1,-1,0,0]
uy = [0,0,1,-1]

T = int(input())

for _ in range(T):
    #지렁이 개수
    stick = 0
    width, height, n = list(map(int,input().split()))
    blocked = [[False] * width for _ in range(height)]
    for _ in range(n):
        x, y = list(map(int,input().split()))
        blocked[y][x] = True

    for y in range(height):
        for x in range(width):
            if(blocked[y][x]):
                start = [y,x]
                #bfs 시작
                queue = []
                queue.append(start)
                blocked[y][x] = False
                while(len(queue)):
                    ny, nx = queue.pop(0)
                    for i in range(4):
                        rx = nx + ux[i]
                        ry = ny + uy[i]
                        if(rx>=0 and rx<width and ry>=0 and ry <height and blocked[ry][rx]):
                            queue.append([ry,rx])
                            blocked[ry][rx]= False

                stick+=1
            
    sticks.append(stick)
            

for i in sticks:
    print(i)