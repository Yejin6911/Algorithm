dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
dir = ['U', 'D', 'R', 'L']


def solution(dirs):
    answer = 0
    visited = {(0, 0): []}
    x, y = 0, 0
    for d in dirs:
        i = dir.index(d)
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        else:
            if (nx, ny) not in visited[(x, y)]:
                if (nx, ny) in visited.keys() and (x, y) in visited[(nx, ny)]:
                    continue
                visited[(x, y)].append((nx, ny))
                answer += 1
            x, y = nx, ny
            if (x, y) not in visited.keys():
                visited[(nx, ny)] = []
    return answer


print(solution("ULURRDLLU"))
