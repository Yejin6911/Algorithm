# https://programmers.co.kr/learn/courses/30/lessons/60058 - 다시 풀어보기!
# 균형잡힌 괄호 문자열의 인덱스 반환
def get_u(p):
    count = 0
    for i in range(len(p)):
        if p[i] == "(":
            count += 1
        elif p[i] == ")":
            count -= 1
        if count == 0:
            return i+1

# 올바른 괄호 문자열인지 판단


def check(p):
    count = 0
    for i in p:
        if i == "(":
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    # 1
    if p == '':
        return answer
    # 2
    index = get_u(p)
    u = p[0:index]
    v = p[index:]
    # 3
    if check(u):
        answer = u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
