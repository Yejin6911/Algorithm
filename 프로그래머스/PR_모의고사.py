def solution(answers):
    answer = []    
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    len_a = len(a)
    len_b = len(b)
    len_c = len(c)
    count = [0,0,0]
    for i in range(len(answers)):
        if a[i%len_a] == answers[i]:
            count[0] +=1
        if b[i%len_b] == answers[i]:
            count[1] +=1
        if c[i%len_c] == answers[i]:
            count[2] +=1   
    Max = max(count)
    for i in range(len(count)):
        if count[i] == Max:
            answer.append(i+1)
    answer.sort()
    return answer

solution([1,2,3,4,5])