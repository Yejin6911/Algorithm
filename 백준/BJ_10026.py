import copy
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y, = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and matrix[nx][ny] == matrix[x][y]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


result_1 = 0
visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result_1 += 1
            bfs(i, j)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

result_2 = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            result_2 += 1
            bfs(i, j)

print(result_1, result_2)
