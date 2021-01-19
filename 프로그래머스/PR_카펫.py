def solution(brown, yellow):
    answer = []
    for i in range(1, yellow+1):
        x = i
        if yellow % x == 0:
            y = yellow//x
        if 4+2*x+2*y == brown:
            answer.append(x+2)
            answer.append(y+2)
            break
    answer.sort(reverse=True)
    return answer
