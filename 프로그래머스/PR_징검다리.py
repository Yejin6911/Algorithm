def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start = 0
    end = distance
    # 이분탐색 시작
    while start <= end:
        # 중간값 구하기
        mid = int((start+end)/2)
        min_distance = distance
        count = 0  # 제거한 징검다리의 갯수
        now = 0  # 현재 시작 위치
        for rock in rocks:
            diff = rock-now
            # 거리가 설정한 최솟값보다 작을 경우 징검다리 제거
            if diff < mid:
                count += 1
            # 거리가 최소값보다 크거나 같을 경우
            else:
                # 현재 바위 위치로 시작점 변경
                now = rock
                # 최소값 update
                min_distance = min(min_distance, diff)
        # 제거 갯수가 n보다 클 경우 기준 줄이기
        if count > n:
            end = mid - 1
        # 제거 갯수가 n보다 크거나 같을 경우
        else:
            answer = min_distance
            start = mid + 1
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))
