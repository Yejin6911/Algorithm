def check(time, line):
    cnt = 0
    # 구간 설정
    start = time
    end = time+1000
    for i in line:
        if i[1] >= start and i[0] < end:
            cnt += 1
    return cnt


def solution(lines):
    new_lines = []
    for line in lines:
        date, s, t = line.split()
        s = s.split(':')
        # 소요 시간 밀리 초로 변경
        t = float(t.replace('s', ''))*1000
        # 끝나는 시간 초로 변경 후 밀리초로 변경
        end = (int(s[0])*3600+int(s[1])*60 + float(s[2]))*1000
        # 0.001초 = 1밀리초
        start = end-(t-1)
        new_lines.append((start, end))
    answer = 0
    # 요청량이 변하는 순간은 각 로그의 시작과 끝이기 때문에 해당 값들에서만 비교해주면 O(n^2)로 답을 구할 수 있다.
    for line in new_lines:
        answer = max(answer, check(
            line[0], new_lines), check(line[1], new_lines))
    return answer
