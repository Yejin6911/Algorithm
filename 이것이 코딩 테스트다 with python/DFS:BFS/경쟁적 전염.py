import sys
from queue import PriorityQueue
from collections import deque


n, k = map(int, sys.stdin.readline().rstrip().split())

graph = []  # 전체 보드 정보를 담는 리스트
data = []  # 바이러스에 대한 저보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        # 해당 위치에 바이러스 존재하는 경우
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))  # 바이러스 종류, 시간, 위치 X, 위치 Y

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
queue = deque(data)
s, x, y = map(int, sys.stdin.readline().rstrip().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

# 너비우선탐색(BFS)진행
while queue:
    virus, now_s, now_x, now_y = queue.popleft()
    # s초가 지나가거나 큐가 빌 때까지 반복
    if now_s == s:
        break
    # 현재 노드에서 주변 4개의 위치 확인
    for i in range(4):
        nx = now_x + dx[i]
        ny = now_y + dy[i]
        # 해당 위치로 갈 수 없는 경우
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 갈 수 있고 아직 비어있는 위치라면 바이러스 넣기
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            queue.append((graph[nx][ny], now_s+1, nx, ny))

print(graph[x-1][y-1])
