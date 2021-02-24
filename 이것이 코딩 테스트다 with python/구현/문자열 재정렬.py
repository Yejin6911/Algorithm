import sys

n = sys.stdin.readline().rstrip()

A = []
B = []
for i in n:
    if i.isalpha():
        A.append(i)
    else:
        B.append(int(i))
A.sort()
for a in A:
    print(a, end='')
# 이부분 주의! 숫자가 없을 때는 출력X
if len(B):
    print(sum(B))
