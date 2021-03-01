from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for x in range(n)]


# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    # queue 구현을 위해 deque 라이브러리 사용
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 해당 공간을 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if matrix[nx][ny] == 0:
                continue
            # 해당 칸을 처음 방문 하는 경우에만 최단거리 기록
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y]+1
                queue.append((nx, ny))
    # 가장 마지막 칸 최단거리 출력
    return matrix[n-1][m-1]


print(bfs(0, 0))
