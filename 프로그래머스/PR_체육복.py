# set사용하여 전처리
def solution(n, lost, reserve):
    answer = 0
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    answer = n-len(set_lost)
    return answer

# list comprehension으로 전처리
# def solution(n, lost, reserve):
#     answer = 0
#     new_lost = [x for x in lost if x not in reserve]
#     new_reserve = [x for x in reserve if x not in lost]
#     for i in new_reserve:
#         if i-1 in new_lost:
#             new_lost.remove(i-1)
#         elif i+1 in new_lost:
#             new_lost.remove(i+1)
#     answer = n-len(new_lost)
#     return answer


print(solution(5, [2, 4], [1, 3, 5]))
