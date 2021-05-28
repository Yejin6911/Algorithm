import sys

input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().rstrip().split())
    data = []
    for _ in range(m):
        a, b = map(int, input().rstrip().split())
        data.append((a, b))
    data.sort(key=lambda x: x[1])
    books = [0 for _ in range(n+1)]
    cnt = 0
    for d in data:
        if cnt == m:
            break
        for i in range(d[0], d[1]+1):
            if not books[i]:
                books[i] = 1
                cnt += 1
                break
    print(cnt)
