# https://www.acmicpc.net/submit/18352

from collections import deque
import sys
INF = 999999

# 틀린 이유 알아보기
n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
distance = [INF for x in range(n+1)]

graph = [[] for x in range(n+1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)


def dfs(index):
    d = distance[index]+1
    for node in graph[index]:
        if distance[node] > d:
            distance[node] = d
            dfs(node)
    return


distance[x] = 0
dfs(x)
result = []
for i in range(len(distance)):
    if distance[i] == k:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    for i in result:
        print(i)


#책풀이 - bfs

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for x in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)

# 모든 도시에 대한 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0  # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색 실행
q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now]+1
            q.append(next_node)
# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
