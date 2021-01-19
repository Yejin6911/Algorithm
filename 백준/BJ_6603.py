import sys
# #방법 1 - dfs 사용해서 풀기
def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
combi = [0 for i in range(13)]

while True:
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()


#방법 2 - combination 라이브러리 사용

from itertools import combinations

while True:
    s = list(map(int, sys.stdin.readline().rstrip().split()))
    if s[0] == 0: 
        break
    del s[0]
    s = list(combinations(s, 6))

    for i in s:
        for j in i:
            print(j,end=' ')
        print()
    print()
