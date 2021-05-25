import copy
import sys
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 1개 시간초과
# def dfs(x, y, board, visited, d, cost):
#     global answer
#     if x == y == len(board)-1:
#         answer = min(cost, answer)
#         return
#     check = False
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0 <= nx < len(board) and 0 <= ny < len(board) and not board[nx][ny] and not visited[nx][ny]:
#             check = True
#             visited[nx][ny] = 1
#             if i % 2 == d % 2:
#                 dfs(nx, ny, board, visited, i, cost+100)
#             else:
#                 dfs(nx, ny, board, visited, i, cost+600)
#             visited[nx][ny] = 0
#     if not check:
#         return


# def solution(board):
#     global answer
#     answer = sys.maxsize
#     visited = [[0]*len(board) for _ in range(len(board))]
#     x, y = 0, 0
#     visited[x][y] = 1
#     for i in range(4):
#         nx = x+dx[i]
#         ny = y+dy[i]
#         if 0 <= nx < len(board) and 0 <= ny < len(board) and not board[nx][ny] and not visited[nx][ny]:
#             visited[nx][ny] = 1
#             dfs(nx, ny, board, visited, i, 100)
#             visited[nx][ny] = 0
#     return answer

# def bfs(start, board):
#     costs = [[0]*len(board) for _ in range(len(board))]
#     queue = deque()
#     queue.append()
#     while queue:
#         x, y, d = queue.popleft()
#         if x == len(board)-1 and y == len(board)-1:
#             answer = min(costs[x][y], answer)
#             return
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if not (nx == 0 and ny == 0) and 0 <= nx < len(board) and 0 <= ny < len(board) and not board[nx][ny]:
#                 if d % 2 == i % 2:
#                     new_cost = costs[x][y]+100
#                 else:
#                     new_cost = costs[x][y]+600
#                 if costs[nx][ny] == 0 or costs[nx][ny] >= new_cost:
#                     costs[nx][ny] = new_cost
#                     queue.append((nx, ny, i))
#     return board[-1][-1]


def solution(n, start, end, roads, traps):
    dist = [[[] for _ in range(n)] for _ in range(n)]
    for road in roads:
        dist[road[0]-1][road[1]-1].append(road[2])
        # 길 여러개인 경우
        if len(dist[road[0]-1][road[1]-1]) > 1:
            dist[road[0]-1][road[1]-1].sort()
    start -= 1
    end -= 1
    queue = deque()
    queue.append((start, 0, dist))
    finish = False
    while queue:
        length = len(queue)
        for _ in range(length):
            now, time, dist = queue.popleft()
            if now == end:
                finish = True
                break
            now_dist = copy.deepcopy(dist)
            if now+1 in traps:
                for i in range(n):
                    if len(now_dist[now][i]):
                        now_dist[i][now], now_dist[now][i] = now_dist[now][i], now_dist[i][now]
                    elif len(dist[i][now]):
                        now_dist[i][now], now_dist[now][i] = now_dist[now][i], now_dist[i][now]
            for i in range(n):
                if i != now and len(now_dist[now][i]):
                    queue.append((i, time+now_dist[now][i][0], now_dist))
        if finish:
            return time


print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [
      1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
