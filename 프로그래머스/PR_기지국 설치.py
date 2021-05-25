import math


def solution(n, stations, w):
    answer = 0
    distance = []
    distance.append(stations[0]-w-1)
    for i in range(len(stations)-1):
        d = (stations[i+1]-w)-(stations[i]+w)-1
        distance.append(d)
    distance.append(n-(stations[-1]+w))

    for d in distance:
        if d > 0:
            answer += math.ceil(d/(w*2+1))
    return answer
