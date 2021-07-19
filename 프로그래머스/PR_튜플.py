def solution(s):
    s = s[1:len(s)-1]
    s = s.split(',')
    new_s = []
    for i in s:
        i = i[1:len(i)-1]
        new_list = [int(x) for x in i.split(',')]
        new_s.append(new_list)
    new_s.sort(key=len)
    answer = []
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
