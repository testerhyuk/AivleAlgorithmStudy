test_case = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(test_case):
    m, n, k = map(int, input().split())
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                cnt += 1
                stack = [[i, j]]

                while stack:
                    y, x = stack.pop()
                    visited[y][x] = True

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < m and 0 <= ny < n:
                            if matrix[ny][nx] == 1 and not visited[ny][nx]:
                                stack.append([ny, nx])

    print(cnt)
