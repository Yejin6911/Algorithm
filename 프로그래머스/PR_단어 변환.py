# 깊이 우선탐색 이용
def bfs(begin, target, words, visited):
    global answer
    answer = 0
    # 스택에 시작원소 넣기
    stack = [begin]

    # 스택에 원소가 있는 동안 계속 탐색 진행
    while(stack):
        now = stack.pop()
        if now == target:
            return answer
        for word in words:
            count = 0
            # 다른 문자 갯수 계산
            for i in range(len(word)):
                if now[i] != word[i]:
                    count += 1
            if count == 1:
                if visited[words.index(word)] != 0:
                    continue
                    # 아직 방문 안한 원소일 경우 방문 표시 후 스택에 push
                visited[words.index(word)] = 1
                stack.append(word)
        answer += 1


def solution(begin, target, words):
    if target not in words:
        return 0
    global answer
    visited = [0 for i in range(len(words))]
    bfs(begin, target, words, visited)
    print(answer)
    return answer


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
