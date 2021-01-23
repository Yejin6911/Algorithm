import sys

# 유클리드 호제법 사용


def gcd(M, N):
    if M < N:
        M, N = N, M
    # gcd(M,0)인 경우
    if N == 0:
        return M
    temp = M % N
    # 나누어 떨어지지 않을 경우
    if temp != 0:
        M = N
        N = temp
        # 반복 진행
        return gcd(M, N)
    # 나누어 떨어지는 경우
    else:
        return N


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().rstrip().split())
    gcd = gcd(M, N)
    # 최대공약수
    print(gcd)
    # 최소공배수
    print(gcd*(M//gcd)*(N//gcd))
