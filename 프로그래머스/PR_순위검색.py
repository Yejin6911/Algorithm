from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    for i in range(len(info)):
        info[i] = info[i].split()
    for i in range(len(query)):
        query[i] = query[i].split(" ")
        query[i] = [x for x in query[i] if x != 'and']
    answer = []
    for q in query:
        total = 0
        for p in info:
            cnt = 0
            for i in range(4):
                if q[i] == '-':
                    cnt += 1
                    continue
                elif q[i] == p[i]:
                    cnt += 1
                else:
                    break
            if cnt == 4 and int(p[4]) >= int(q[4]):
                total += 1
        answer.append(total)
    return answer


# 효율성 통과 코드
def make_all_cases(temp):
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += temp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases


def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(i.split())
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else:
                all_people[case].append(int(seperate_info[4]))

    for key in all_people.keys():
        # 점수 작은 순서대로 정렬
        all_people[key].sort()

    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_people.keys():
            # biesect_left: 이진탐색으로 두번쨰 인자가 들어갈 수 있는 왼쪽의 인덱스 값을 반환해줌
            answer.append(len(all_people[target]) - bisect_left(
                all_people[target], int(seperate_q[7]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)

    return answer
