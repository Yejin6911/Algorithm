def solution(numbers, hand):
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (
        1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left, right = keypad['*'], keypad['#']
    answer = ''
    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left = keypad[n]
        elif n in [3, 6, 9]:
            answer += 'R'
            right = keypad[n]
        else:
            dist_l = abs(left[0]-keypad[n][0])+abs(left[1]-keypad[n][1])
            dist_r = abs(right[0]-keypad[n][0])+abs(right[1]-keypad[n][1])
            if dist_l > dist_r:
                answer += 'R'
                right = keypad[n]
            elif dist_l < dist_r:
                answer += 'L'
                left = keypad[n]
            else:
                if hand == 'right':
                    answer += 'R'
                    right = keypad[n]
                else:
                    answer += 'L'
                    left = keypad[n]
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
