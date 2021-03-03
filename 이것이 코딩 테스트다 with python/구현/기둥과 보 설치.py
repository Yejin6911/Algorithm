def check(answer):
    for x, y, a in answer:
        # 기둥일때
        if a == 0:
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            return False
        # 보일때
        elif a == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    global result
    answer = []
    for frame in build_frame:
        x, y, a, b = frame
        if b == 1:
            new = [x, y, a]
            answer.append(new)
            if not check(answer):
                answer.remove(new)
        elif b == 0:
            new = [x, y, a]
            answer.remove(new)
            if not check(answer):
                answer.append(new)
    return sorted(answer)
