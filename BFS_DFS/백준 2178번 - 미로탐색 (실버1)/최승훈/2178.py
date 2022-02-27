#https://www.acmicpc.net/problem/2178

wh = input()
height, width = int(wh.split(" ")[0]), int(wh.split(" ")[1])

#그래프 입력
blocked = []
#노드 간 거리
distance = []
#이동
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


for _ in range(height):
    temp = list(input())
    blocked.append(temp)
    distance.append([-1] * len(temp))


queue = [[0,0]]
distance[0][0] = 1
    
while(len(queue)):
    #shift
    [y,x] = queue.pop(0)
    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]
        if(ry < height and ry > -1 and rx < width and rx > -1 and blocked[ry][rx] == "1" and distance[ry][rx] == -1):
            queue.append([ry,rx]) # 다음 queue 대입
            distance[ry][rx] = distance[y][x] + 1 #전 이동거리 + 1

result= distance[height -1 ][width - 1]
print(result)


