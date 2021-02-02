def solution(number, k):
    answer = ''
    stack = [number[0]]
    left = ''
    for num in number[1:]:
        # 들어오는 값이 stack 의 끝 값보다 크면 stack값을 제거한다
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        # 새로운 값을 삽입
        stack.append(num)
    if k != 0:
        # 값을 큰 순서대로 넣었기 때문에 제거 안한만큼 스택 뒤에서 제거해주면 된다.
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer


solution("4177252841", 4)
