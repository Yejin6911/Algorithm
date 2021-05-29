def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if not len(stack):
        return 1
    else:
        return 0
