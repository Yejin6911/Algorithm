def dfs(begin, target, words, now):
    global answer
    if begin == target:
        answer = max(now, answer)
        return
    arr = []
    for word in words:
        count = 0
        for i in range(len(word)):
            if begin[i] != word[i]:
                count += 1
        if count == 1:
            arr.append(word)
    for word in arr:
        dfs(word, target, words, now+1)


def solution(begin, target, words):
    if target not in words:
        return 0
    global answer
    answer = 0
    dfs(begin, target, words, 0)
    return answer


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
