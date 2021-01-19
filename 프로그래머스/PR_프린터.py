#프린터
from collections import deque
def solution(priorities, location):
    priorities = deque(priorities)
    count = 0

    while location != -1:
        temp = priorities.popleft()
        location-=1
        now = True
        for i in priorities:
            if i > temp:
                now = False
                break
        if now:
            count +=1
        else:
            priorities.append(temp)
            if location==-1:
                location = len(priorities)+location
    return count