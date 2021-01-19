
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.sort()

    isPrime = [True for x in range(arr[-1]+1)]
    isPrime[1] = False
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(arr[-1] ** 0.5)

    for i in range(2, m+1):
        if isPrime[i] == True:
            for j in range(i+i, arr[-1]+1, i):
                isPrime[j] = False
    count = 0
    for i in arr:
        if isPrime[i] == True:
            count += 1
    print(count)
