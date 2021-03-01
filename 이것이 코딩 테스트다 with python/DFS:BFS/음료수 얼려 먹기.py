import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for x in range(n)]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문


def dfs(row, col):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if row < 0 or row >= n or col < 0 or col >= m:
        return False
    # 현재 노드를 아직 방문하지 않은경우 해당노드 방문 처리
    if matrix[row][col] == 0:
        matrix[row][col] = 1
        # 인접 노드들 모두 재귀적으로 호출
        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)
        return True
    return False


# 모든 노드에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
