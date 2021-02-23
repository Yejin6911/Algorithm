
import sys

s = sys.stdin.readline().rstrip()

count_0 = 0
count_1 = 0

now = s[0]
for i in s:
    if now == i:
        continue
    else:
        # 앞 숫자와 다른 숫자가 나온 경우
        if now == '0':
            count_0 += 1
        elif now == '1':
            count_1 += 1
        now = i
print(min(count_0, count_1))
