import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

count = [0 for _ in range(m)]

for i in data:
    count[i-1] += 1

temp = 0
for i in count:
    if i != 0:
        temp += i*(i-1)/2

result = int(n*(n-1)/2 - temp)

print(result)

# 책 풀이
# A가 선택하는 무게  공의 개수 * 이 때 b가 선택하는 경우의 수

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0]*11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    n -= array[i]
    result += array[i]*n  # B가 선택하는 경우의 수와 곱하기

print(result)
