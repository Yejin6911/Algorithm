import sys

M, N = map(int, sys.stdin.readline().rstrip().split())

isPrime = [True] * (N+1)
isPrime[0] = False
isPrime[1] = False
temp = int(N**0.5)

# 에라토스테네스의 채 원리 이용
for i in range(2, temp+1):
    # 해당 숫자가 소수일 경우
    if isPrime[i] == True:
        # 해당 소수의 배수인 수들을 모두 배제
        for j in range(i+i, N+1, i):
            isPrime[j] = False

for i in range(M, N+1):
    if isPrime[i]:
        print(i)
