import sys   
#1. dfs 이용

def dfs(start, total):
    global count
    if start >= n:
        return
    total += a[start]
    if total == s:
        count += 1
    dfs(start+1, total-a[start]) # 시작점 제외
    dfs(start+1, total) #시작점 포함
    
if __name__ == "__main__":
    n,s = map(int, sys.stdin.readline().rstrip().split())
    a =list(map(int, sys.stdin.readline().rstrip().split()))    
    count= 0
    dfs(0,0)
    print(count)

#2. 조합 이용    
from itertools import combinations
n,s = map(int, sys.stdin.readline().rstrip().split())
a =list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
for i in range(1,len(a)+1):
    c = list(combinations(a,i))
    for j in c:
        if sum(j) == s:
            count+=1
print(count) 


    