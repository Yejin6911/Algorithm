from collections import deque, defaultdict
import math
import sys
sys.setrecursionlimit(10**6)


def find_parent(x, parent):
    if x == parent[x]:
        return x
    else:
        p = find_parent(parent[x], parent)
        parent[x] = p
        return p


def union_find(x, y, parent):
    x = find_parent(x, parent)
    y = find_parent(y, parent)
    parent[y] = x


def bfs(land, start, visited, height, group):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append(start)
    while queue:
        y, x = queue.popleft()
        visited[y][x] = group
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < len(land) and 0 <= nx < len(land[0]) and visited[ny][nx] == 0 and abs(land[ny][nx] - land[y][x]) <= height:
                visited[ny][nx] = group
                queue.append((ny, nx))


def find_height(land, height, table, visited):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for y in range(len(land)):
        for x in range(len(land[0])):
            # 왼쪽 값과 비교
            if x+1 < len(land[0]) and visited[y][x] != visited[y][x+1]:
                a, b = min(visited[y][x], visited[y][x+1]
                           ), max(visited[y][x], visited[y][x+1])
                table[(a, b)] = min(table[(a, b)],
                                    abs(land[y][x] - land[y][x+1]))
            if y+1 < len(land[0]) and visited[y+1][x] != visited[y][x]:
                a, b = min(visited[y+1][x], visited[y][x]
                           ), max(visited[y+1][x], visited[y][x])
                table[(a, b)] = min(table[(a, b)],
                                    abs(land[y+1][x] - land[y][x]))


def solution(land, height):
    visited = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]
    answer = 0
    group = 1

    # 1. land height별로 그룹핑
    for y in range(len(land)):
        for x in range(len(land[0])):
            if visited[y][x] == 0:
                bfs(land, (y, x), visited, height, group)
                group += 1

    # 2. 각 land별로 연결하는 최솟값 찾기
    table = defaultdict(lambda: math.inf)
    find_height(land, height, table, visited)
    table = sorted(table.items(), key=lambda x: x[1])

    nodes = {i: i for i in range(1, group)}
    for (a, b), value in table:
        # 사다리로 연결
        if find_parent(a, nodes) != find_parent(b, nodes):
            union_find(a, b, nodes)
            answer += value
        # 모든 지형이 연결되었는지 확인
        if len(nodes.values()) == 1:
            return answer

    return answer


print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [
      10, 10, 10, 10], [10, 10, 10, 20]], 3))
