import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
sensors = list(map(int, input().rstrip().split()))
sensors.sort()

if k >= n:
    print(0)
else:
    dist = [sensors[i]-sensors[i-1] for i in range(1, n)]
    dist.sort()
    for i in range(k-1):
        dist.pop()

    print(sum(dist))
