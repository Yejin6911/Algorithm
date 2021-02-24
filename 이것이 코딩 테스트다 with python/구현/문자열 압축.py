def solution(s):
    answer = len(s)
    # 문자열 자르는 개수 늘려가며 확인
    for i in range(1, len(s)//2+1):
        result = ''
        now = s[0:0+i]  # 반복 확인할 문자열 추출
        index = i
        count = 1

        # 단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(index, len(s), i):
            # 같은 경우 횟수 증가
            if now == s[j:j+i]:
                count += 1
            # 다른 경우
            else:
                if count == 1:
                    result += now
                else:
                    result = result + str(count)+now
                # 상태 초기화
                now = s[j:j+i]
                count = 1
        # 남아있는 문자열 처리
        if count == 1:
            result += now
        else:
            result = result + str(count)+now
        answer = min(answer, len(result))
    return answer


print(solution("aabbaccc"))
