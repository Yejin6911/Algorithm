import sys

s = sys.stdin.readline().rstrip()

result = 0
for i in s:
    now = int(i)
    if now <= 1 or result == 0:
        result += now
    else:
        if result == 0:
            result += now
        else:
            result *= now

print(result)
