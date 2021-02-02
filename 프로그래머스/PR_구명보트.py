def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people)-1
    # pop을 안쓰는게 효율성 통과하는 방법
    while start <= end:
        answer += 1
        # 두명 태울 수 있는 경우
        if people[start]+people[end] <= limit:
            start += 1
        # 아닐경우 제일 무거운 한사람만 옮김
        end -= 1
    return answer
