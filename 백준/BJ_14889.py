import sys
from itertools import combinations


# 각각 팀원들 끼리의 능력치 합 계산하기
def count(group, array):
    count = 0
    for i in list(combinations(group, 2)):
        count = count + array[i[0]][i[1]] + array[i[1]][i[0]]
    return count


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    array = [list(map(int, sys.stdin.readline().rstrip().split()))
             for x in range(N)]
    people = [x for x in range(N)]
    groups = list(combinations(people, int(N/2)))
    num = len(groups)
    result = []
    # 전체의 앞쪽 반개에 대해서만 반복문 실행 - 리스트의 앞쪽 n번째와 뒤에서 n번째가  나눠지는 그룹이기 때문
    for i in range(int(num/2)):
        group_1 = groups[i]
        group_1_sum = count(group_1, array)
        group_2 = groups[num-1-i]
        group_2_sum = count(group_2, array)
        result.append(abs(group_1_sum-group_2_sum))
    # 최소값 출력
    print(min(result))
