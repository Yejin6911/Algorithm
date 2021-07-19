import heapq


def solution(operations):
    max_heap = []
    min_heap = []

    for op in operations:
        a, b = op.split()
        if a == 'I':
            b = int(b)
            heapq.heappush(max_heap, (-b, b))
            heapq.heappush(min_heap, b)
        else:
            if len(max_heap):
                if b == '1':
                    M = heapq.heappop(max_heap)[1]
                    min_heap.remove(M)
                else:
                    m = heapq.heappop(min_heap)
                    max_heap.remove((-m, m))
    if not max_heap and not min_heap:
        answer = [0, 0]
    else:
        answer = [max_heap[0][1], min_heap[0]]
    return answer


print(solution(["I 7", "I 5", "I -5", "D -1"]))
