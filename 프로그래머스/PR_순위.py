def solution(n, results):
    wins = {}  # key가 이긴 사람들 저장
    loses = {}  # key가 이기지 못한 사람들 저장
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()

    for i in range(1, n+1):
        for win, lose in results:
            # i가 이긴 사람들 저장
            if win == i:
                wins[i].add(lose)
            # i가 진 사람들 저장
            if lose == i:
                loses[i].add(win)
        # i를 이긴 사람들은 i에게 진 사람들을 반드시 이긴다.
        for winner in loses[i]:
            wins[winner].update(wins[i])
        # i에게 진 사람들은 i를 이긴사람들에게 반드시 진다.
        for loser in wins[i]:
            loses[loser].update(loses[i])
    answer = 0
    for i in range(1, n+1):
        if len(wins[i])+len(loses[i]) == n-1:
            answer += 1
    return answer
