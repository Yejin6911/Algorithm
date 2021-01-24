import sys
from itertools import combinations

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    array = []
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))
    # 치킨집 위치와 집의 위치 각각 배열에 저장
    chicken = []
    house = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 2:
                chicken.append((i, j))
            elif array[i][j] == 1:
                house.append((i, j))
    # 치킨집을 선택할 수 있는 조합 구하기
    choices = list(combinations(chicken, m))
    dist = []
    # 선택지 별로 최소 거리 합 구하기
    for choice in choices:
        total = 0
        for h in house:
            temp = []
            for c in choice:
                temp.append(abs(h[0]-c[0])+abs(h[1]-c[1]))
            total += min(temp)
        dist.append(total)
    # 전체 가능한 치킨 거리 중 최소값 출력
    print(min(dist))
