def solution(name):
    name = list(name)
    answer = 0
    index = 0
    while True:
        right = 1
        left = 1
        if name[index] != 'A':
            answer += min(ord(name[index])-ord('A'),
                          (ord('Z')-ord(name[index])+1))

        # 이제 안바꿔도 되니까 A문자 변경해준다. - 일종의 완료 표시
        name[index] = 'A'
        # 이미 모든 문자가 A인경우 반복문 break
        if name == ["A"]*len(name):
            break
            # 왼쪽, 오른쪽 이동 중 A를 더 빨리 만나는 곳 찾기
        for i in range(1, len(name)):
            if name[index+i] == "A":
                right += 1
            else:
                break
        for i in range(1, len(name)):
            if name[index-i] == "A":
                left += i
            else:
                break
                # 왼쪽인경우
        if right > left:
            answer += left
            index -= left
        # 오른쪽인경우
            else:
            answer += right
            index += right
    return answer


solution("JEROEN")
