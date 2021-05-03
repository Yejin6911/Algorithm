def solution(N, number):
    dp = []
    answer = -1

    for i in range(1, 9):
        numbers = []
        numbers.append(int(str(N)*i))

        for j in range(0, i-1):
            for x in dp[j]:
                for y in dp[i-1-j-1]:
                    numbers.append(x+y)
                    numbers.append(x-y)
                    numbers.append(x*y)
                    if y != 0:
                        numbers.append(x//y)
        if number in numbers:
            answer = i
            break

        dp.append(numbers)

    return answer


print(solution(5, 12))
