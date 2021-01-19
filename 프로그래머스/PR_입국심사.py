def solution(n, times):
    answer=0
    #가장 적게 걸리는 곳에서 모든 사람이 검사 받는 경우
    right = min(times) * n
    left = 1
    
    while left <= right:
        mid = (left+right)//2
        count = 0
        
        for time in times:
            #시간 측정
            count += mid // time
            #시간 내에 n명 이상을 측정할 수 있는 경우
            #심사관에게 주어진 시간을 줄여본다
            if count >= n:
                answer = mid
                right = mid-1
                break
        #시간내에  n명을 측정할 수 없는 경우
        if count < n :
            left = mid+1
    return answer