import sys

n, m = map(int, sys.stdin.readline().split())
a, b, d = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for x in range(m)]
visited = [[0]*m for x in range(n)]
visited[a][b] = 1


def change_d(d):
    if d-1 == -1:
        d = 3
    else:
        d -= 1
    return d


def check(new_a, new_b):
    if 0 <= new_a < n and 0 <= new_b < m and map[new_a][new_b] == 0 and visited[new_a][new_b] == 0:
        return True
    else:
        return False


steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]
result = 1
turn_time = 0
while True:
    d = change_d(d)
    new_a = a+steps[d][0]
    new_b = b+steps[d][1]
    if check(new_a, new_b):
        a = new_a
        b = new_b
        turn_time = 0
        result += 1
        visited[a][b] = 1
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        new_a = a-steps[d][0]
        new_b = b-steps[d][1]
        if check(new_a, new_b):
            a = new_a
            b = new_b
            result += 1
            visited[a][b] = 1
        else:
            break
print(result)
