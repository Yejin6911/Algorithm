import sys
from collections import deque

def printer(queue, location):
    count = 0

    while True:
        temp = queue.popleft()
        if any(temp[1] < q[1] for q in queue):
            queue.append(temp)
        else:
            count+=1
            if temp[0]==location:
                return count

if __name__ == "__main__":
    num = int(sys.stdin.readline().rstrip())
    result = []
    for i in range(num):
        n, m = sys.stdin.readline().rstrip().split()
        a = list(map(int,sys.stdin.readline().rstrip().split()))
        a = deque([x for x in enumerate(a)])
        result.append(printer(a, int(m)))
    for i in result:
        print(i)