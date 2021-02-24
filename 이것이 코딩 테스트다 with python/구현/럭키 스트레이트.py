import sys

n = sys.stdin.readline().rstrip()

front = 0
back = 0
for i in range(len(n)):
    # 앞부분인 경우
    if i < len(n)/2:
        front += int(n[i])
    # 뒷부분인 경우
    else:
        back += int(n[i])
if front == back:
    print("LUCKY")
else:
    print("READY")

# 책 풀이 - 합을 저장하는 변수를 하나만 사용했다.
n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length//2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 오른쪽 합 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")
