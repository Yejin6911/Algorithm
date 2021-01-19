def bfs(start, now, numbers, target):
    global answer
    if start == len(numbers):
        if now == target:
            answer+=1
        return
    else:
        bfs(start+1, now+numbers[start], numbers, target)
        bfs(start+1, now-numbers[start], numbers, target)
    
def solution(numbers, target):
    global answer 
    answer = 0
    bfs(0,0,numbers,target)
    return answer

solution([1, 1, 1, 1, 1],3)