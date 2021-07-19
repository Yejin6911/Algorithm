from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = 1
    answer = 0
    while queue:
        x, y, dist = queue.popleft()
        if x == n-1 and y == m-1:
            answer = dist
            break
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, dist+1))
    if answer == 0:
        answer = -1
    return answer
