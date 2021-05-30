import heapq


def solution(jobs):
    answer = 0
    now, i = 0, 0
    start = -1
    heap = []
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            current = heapq.heappop(heqp)
            start = now
            now += current[0]
            answer += (now-current[1])
            i += 1
        else:
            now += 1
    answer = int(answer/len(jobs))
    return answer


print(solution([[0, 3], [1, 9], [2, 6]]))
