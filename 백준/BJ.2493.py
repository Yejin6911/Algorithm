import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int, input().rstrip().split()))

stack = []
for i in range(len(data)):
    while stack:
        if data[i] <= data[stack[-1]]:
            print(stack[-1]+1, end=' ')
            stack.append(i)
            break
        else:
            stack.pop()
    if not len(stack):
        print(0, end=' ')
        stack.append(i)
