import sys
from heapq import heappush, heappop

INF = sys.maxsize
graph = [[]]


# 방법 1 - 다익스트라 알고리즘
def dijkstra(src, dst):
    global graph
    n = len(graph)
    distance = [INF for _ in range(n+1)]
    # 시작점부터의 거리 저장
    distance[src] = 0
    # 최단경로 포함되는 점들
    S = [[0, src]]

    while S:
        w, x = heappop(S)
        # 이미 최단경로인 경우
        if distance[x] < w:
            continue
        # 아닌 경우
        for item in graph[x]:
            nx, ncost = item[0], item[1]
            ncost += w
            if ncost < distance[nx]:
                distance[nx] = ncost
                heappush(S, [ncost, nx])
    return distance[dst]


def solution(n, s, a, b, fares):
    global graph
    answer = INF
    graph = [[] for _ in range(n+1)]
    for fare in fares:
        c, d, f = fare
        graph[c].append([d, f])
        graph[d].append([c, f])
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s, i)+dijkstra(i, a)+dijkstra(i, b))

    return answer


# 방법 2 - 플로이드 와샬 알고리즘
def solution(n, s, a, b, fares):
    answer = INF
    global graph
    graph = [[INF]*n for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0

    for fare in fares:
        graph[fare[0] - 1][fare[1] - 1] = fare[2]
        graph[fare[1] - 1][fare[0] - 1] = fare[2]

    # t점을 거쳐서 가는 경로와 i->j 중 최단경로 구하기
    for t in range(n):
        for i in range(n):
            # 갈때 올때 비용이 같아 앞 고려 안해주어도 됨
            for j in range(i, n):
                if i != j:
                    temp = min(graph[i][j], graph[i][t]+graph[t][j])
                    graph[i][j] = graph[j][i] = temp

    for t in range(n):
        temp = graph[s-1][t]+graph[t][b-1]+graph[t][a-1]
        answer = min(answer, temp)

    return answer
