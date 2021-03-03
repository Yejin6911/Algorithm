
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    for i in range(len(prices)):
        price = prices.popleft()
        count = 0
        for j in prices:
            count += 1
            if j < price:
                break
        answer.append(count)
    return answer
