import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = []
for i in range(n):
    start, end = map(int, input().rstrip().split())
    data.append((start, end))

data.sort(key=lambda x: (x[1], x[0]))
now = 0
cnt = 1
for i in range(1, n):
    if data[i][0] >= data[now][1]:
        now = i
        cnt += 1

print(cnt)
