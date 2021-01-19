import sys
from collections import deque

if __name__ == "__main__":
    n,k = map(int, sys.stdin.readline().rstrip().split())
    a = deque([x for x in range(1,n+1)])
    result = []
    now = 1
    while len(a):
        if now%k==0:
            result.append(a.popleft())
            now+=1
        else:
            a.append(a.popleft())
            now+=1
        
    print('<',end='')
    for i in range(n):
        if i==(n-1):
            print(str(result[i]),end='>')
        else:
            print(str(result[i]), end=', ')