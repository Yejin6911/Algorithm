import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

row = [-1, +1, 0, 0]
col = [0, 0, -1, +1]
queue = deque()
queue.append((0, 0))

while queue:
    now = queue.popleft()

    for i in range(4):
        # 미로 범위를 벗어나는 경우 제외
        if now[0]+row[i] < 0 or now[0]+row[i] >= n or now[1]+col[i] < 0 or now[1]+col[i] >= m:
            continue
        new_row = now[0]+row[i]
        new_col = now[1]+col[i]
        # 빈 공간인 경우
        if graph[new_row][new_col] == 1:
            queue.append((new_row, new_col))
            graph[new_row][new_col] = graph[now[0]][now[1]]+1

print(graph[n-1][m-1])
