import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()

result = 0
now = 0  # 현재 그룹 내 명수

for i in data:
    now += 1  # 현재 그룹 한명 추가
    if now >= i:  # 현재 인원이 공포수보다 클 때 그룹으로 추가
        result += 1  # 그룹 수 +1
        now = 0  # 현재 인원 초기화

print(result)
