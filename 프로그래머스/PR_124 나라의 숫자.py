def solution(n):
    answer = ''
    data = ['4', '1', '2']
    while n >= 1:
        left = n % 3
        n //= 3
        if left == 0:
            n -= 1
        answer = data[left] + answer

    return answer
