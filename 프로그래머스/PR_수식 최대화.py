from itertools import permutations
import copy


def solution(expression):
    answer = 0
    operators = []
    temp = ''
    new_expression = []
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            new_expression.append(int(temp))
            new_expression.append(i)
            operators.append(i)
            temp = ''
    new_expression.append(int(temp))
    operators = list(set(operators))
    priorities = list(permutations(operators, len(operators)))

    for p in priorities:
        temp = copy.deepcopy(new_expression)
        for op in p:
            while True:
                if op not in temp:
                    break
                index = temp.index(op)
                n1, n2 = temp[index-1], temp[index+1]
                if temp[index] == '+':
                    new = n1+n2
                elif temp[index] == '-':
                    new = n1-n2
                else:
                    new = n1*n2
                if len(temp) == 3:
                    temp = [new]
                else:
                    temp = temp[:index-1] + \
                        [new]+temp[index+2:]
        answer = max(answer, abs(temp[0]))
    return answer


print(solution("50*6-3*2"))
