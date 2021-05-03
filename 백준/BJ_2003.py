import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
A = list(map(int, input().rstrip().split()))

start, end = 0, 0
total = A[start]
cnt = 0
while True:
    if total < m:
        end += 1
        if end == n:
            break
        total += A[end]
    elif total >= m:
        if total == m:
            cnt += 1
        if start == end:
            start += 1
            end += 1
            if end == n:
                break
            total = A[start]
        else:
            total -= A[start]
            start += 1

print(cnt)
