def solution(triangle):
    answer = 0
    dp = [[triangle[0][0]]]
    for row in range(1, len(triangle)):
        S = []
        for i in range(0, len(triangle[row])):
            if i == 0:
                S.append(dp[row-1][i]+triangle[row][i])
            elif i == len(triangle[row])-1:
                S.append(dp[row-1][i-1]+triangle[row][i])
            else:
                S.append(max(dp[row-1][i-1]+triangle[row]
                             [i], dp[row-1][i]+triangle[row][i]))
        dp.append(S)
    answer = max(dp[-1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
