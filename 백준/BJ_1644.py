import sys

# N보다 작은 소수 리스트 구하는 함수


def primeList(N):
    prime = []
    isPrime = [True] * (N+1)
    isPrime[0] = False
    isPrime[1] = False
    temp = int(N**0.5)

    for i in range(2, temp+1):
        if isPrime[i] == True:
            for j in range(i+i, N+1, i):
                isPrime[j] = False
    for i in range(len(isPrime)):
        if isPrime[i] == True:
            prime.append(i)
    return prime


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    prime = primeList(N)
    sum = 0
    index = 0
    now = []
    count = 0
    while index < len(prime):
        if sum == N:
            count += 1
            sum -= now.pop(0)
        else:
            if sum+prime[index] <= N:
                sum += prime[index]
                now.append(prime[index])
                index += 1
            else:
                sum -= now.pop(0)
                # 마지막 숫자가 now에 남아 있는 경우 고려
    while now:
        if sum == N:
            count += 1
        now.pop(0)
    print(count)
