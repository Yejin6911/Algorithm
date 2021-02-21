import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
now = n
count = 0
while now != 1:
    if now % k == 0:
        n //= k
    else:
        now -= 1
    count += 1
print(count)

# 책 풀이 1
n, k = map(int, sys.stdin.readline().rstrip().split())
result = 0

# N이 K이상이라면 K로 계속 나누기
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1
print(result)


# 책 풀이 2 - n 이 매우 큰 경우 효율성 고려하는 코드
n, k = map(int, sys.stdin.readline().rstrip().split())
result = 0

while True:
    # (n==k로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n//k)*k
    result += (n-target)
    n = target
    # n이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
