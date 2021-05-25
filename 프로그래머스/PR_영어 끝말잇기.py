import sys
from heapq import heappush, heappop
INF = sys.maxsize

# 다이젝스트라 알고리즘


def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])
    # 시작점부터의 시간 저장
    time = [INF for _ in range(N+1)]
    time[1] = 0
    included = [[0, 1]]  # [시간,위치]
    while included:
        w, x = heappop(included)
        # 이미 최단시간
        if time[x] < w:
            continue
        # 아닌 경우
        for item in graph[x]:
            nx, ntime = item[0], item[1]
            ntime += w
            if ntime < time[nx]:
                time[nx] = ntime
                heappush(included, [ntime, nx])
    answer = 0
    for t in time:
        if t <= 3:
            answer += 1
    return answer


solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
         3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)
