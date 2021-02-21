import sys
from typing import Mapping
n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split()))
          for x in range(n)]
temp = 0
index = -1
for i in range(len(matrix)):
    if temp < min(matrix[i]):
        temp = min(matrix[i])
        index = i
print(min(matrix[index]))


# 책 풀이 1
result = 0
for i in range(n):
    # 한 줄씩 입력받아 확인
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수 들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)

# 책 풀이 2
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)
