from collections import deque
import sys

sys.stdin = open('input.txt', 'r')

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, farm):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        farm[x][y] = 0
        
        for i in range(4):
            mov_x = x + dx[i]
            mov_y = y + dy[i]

            if mov_x >= 0 and mov_y >= 0 and mov_x < n and mov_y < m and farm[mov_x][mov_y] == 1:
                queue.append((mov_x, mov_y))
                farm[mov_x][mov_y] = 0
    return 1

for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0] * m for i in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        farm[y][x] = 1
    
    cnt = 0

    for x in range(n):
        for y in range(m):
            if farm[x][y] == 1:
                cnt += bfs(x, y, farm)
    print(cnt)