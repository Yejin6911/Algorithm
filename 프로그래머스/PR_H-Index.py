def solution(citations):
    citations.sort()
    h = len(citations)
    while True:
        for i in range(len(citations)-1,-1,-1): 
        #enumerate 사용하면 더 편함
        #for i, value in enumerate(citations)
            if citations[i] >= h and len(citations[i:]) >= h:
                return h
        else:
            h-=1           
    return h

print(solution([3, 0, 6, 1, 5]))