from collections import defaultdict


def solution(tickets):
    stack = ["ICN"]
    answer = []
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
    for r in routes:
        routes[r].sort()
    while stack:
        now = stack[-1]
        if now not in routes or len(routes[now]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(routes[now].pop(0))
    return answer[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], [
    "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
