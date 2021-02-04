import sys

# 유클리드 호제법 이용


def gcd(arr):
    def g(x, y):
        # y가 0이 아닐 때까지
        while y:
            x, y = y, x % y
        return x
    a = arr[0]
    for b in arr[1:]:
        a = g(a, b)
    return a


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    T = [int(sys.stdin.readline().rstrip()) for x in range(n)]
    diff = []
    for i in range(1, len(T)):
        diff.append(T[i]-T[i-1])
    # 나무 사이 거리 중 중복 제거
    set_diff = list(set(diff))
    set_diff.sort(reverse=True)
    # 최대공약수 구하기
    gcd = gcd(set_diff)

    answer = 0
    for d in diff:
        if d != gcd:
            # 새로 심을 나무 갯수 더해주기
            answer += (d//gcd-1)
    print(answer)
