from collections import deque


def solution(n, edge):
    data = [[] for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]
    # 간선 정보 저장
    for a, b in edge:
        data[a].append(b)
        data[b].append(a)
    # 큐 생성(너비 우선 탐색)
    queue = deque()
    queue.append((1, 0))
    visited[1] = 0
    while queue:
        now = queue.popleft()
        for node in data[now[0]]:
            if visited[node] == -1:
                visited[node] = now[1]+1
                queue.append((node, visited[node]))
    M = max(visited)
    answer = visited.count(M)
    return answer
