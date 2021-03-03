import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
city = [list(map(int, sys.stdin.readline().rstrip().split()))
        for x in range(n)]

# 치킨집 구하기
chicken = []
houses = []

for row in range(n):
    for col in range(n):
        if city[row][col] == 1:
            houses.append((row, col))
        elif city[row][col] == 2:
            chicken.append((row, col))

choices = list(combinations(chicken, m))
result = 9999
for choice in choices:
    sum = 0
    for house in houses:
        dist = []
        for chicken in choice:
            dist.append(abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
        sum += min(dist)
    result = min(result, sum)

print(result)
