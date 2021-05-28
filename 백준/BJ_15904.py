import sys

input = sys.stdin.readline

S = input().rstrip()

ucpc = "UCPC"
now = 0
result = True
temp = S
for i in range(4):
    if ucpc[i] in temp:
        idx = temp.index(ucpc[i])
        temp = temp[idx+1:]
    else:
        result = False
        break
if result:
    print("I love UCPC")
else:
    print("I hate UCPC")
