import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    # 양방향이기 때문에 양쪽에 다 넣어주어야 한다.
    graph[v1].append(v2)
    graph[v2].append(v1)

# 숫자가 작은 점부터 조회할 수 있도록 정렬처리해주었다.
for i in graph:
    i.sort()


# 깊이우선탐색
def dfs(graph, v, visited):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 너비우선탐색
def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False for _ in range(n+1)]
dfs(graph, v, visited)
for i in range(1, n+1):
    if not visited[v]:
        dfs(i)
print()

visited = [False for x in range(n+1)]
bfs(graph, v, visited)
for i in range(1, n+1):
    if not visited[v]:
        bfs(i)
