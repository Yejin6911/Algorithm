import sys

n, m, k = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))

num.sort(reverse=True)
num = num[0:2]
# count = 0
result = 0
count = 0

while count < m:
    for i in range(k):
        result += num[0]
        count += 1
        if count == m:
            break
    # 이부분을 생각 못해서 틀렸었다.
    # 두 번째 큰 수는 최소한만 더해주면 된다.
    result += num[1]
    count += 1
print(result)

# 책 답안
first = num[0]  # 가장 큰 수
second = num[1]  # 두번 째 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)
