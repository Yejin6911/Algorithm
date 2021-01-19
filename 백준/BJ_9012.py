import sys

#내 풀이
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    a = [sys.stdin.readline().rstrip() for x in range(n)]
    for i in a:
        i = list(i)
        stack = []
        for j in i:
            if j == '(':
                stack.append(j)
            elif j == ')':
                if len(stack) and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(j)
        if len(stack):
            print("NO")
        else:
            print("YES")

#방법 2_중간에 이미 VPS가 아니면 끝까지 탐색 X
def check(brackets):
    stack = []
    for i in brackets:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return "NO"
            else:
                stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"

#방법3_ stack push pop을 sum을 1더하고 빼는걸로 판단
def check_2(brackets):
    sum = 0
    for i in brackets:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')