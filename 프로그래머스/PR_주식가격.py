# 효율성 다 틀리는 코드
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         price = prices[i]
#         if i==(len(prices)-1):
#             answer.append(0)
#         else:
#             compare=prices[i+1:]
#             time = 0
#             for x in compare:
#                 time+=1
#                 if x < price:
#                     break
#             answer.append(time)
#     return answer

# 개선 1
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         count = 0
#         for j in range(i+1, len(prices)):
#             count+=1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(count)
#     return answer

# 개선 2
# deque 라이브러리 사용
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)
    return answer
