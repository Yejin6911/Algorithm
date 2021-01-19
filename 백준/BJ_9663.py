
#방법 1
import sys

def bfs(sol, n):
    global count
    if len(sol) == n:
        count+=1
        return            
    for i in range(n):
        isPromising = True
        for j in range(len(sol)):
            if sol[j] == i or abs(j-len(sol)) == abs(sol[j]-i):
                isPromising = False
                break
        if isPromising:
            sol.append(i)
            bfs(sol,n)
            sol.pop()

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for i in range(N):
        sol = [i]
        bfs(sol,N)
    print(count)

#방법 2
import sys

def bfs(sol, n):
    global count
    if len(sol) == n:
        count += 1
        return
    candidate = list(range(n)) #n=4인 경우, candidate=[0,1,2,3]
    for i in range(len(sol)): #i는 어쩌면 행 번호
        if sol[i] in candidate:
            candidate.remove(sol[i])
        dist = len(sol) - i
        # sol[i]가 아닌 len(sol)로 하는 이유는, 다음 차례에 들어갈 칸이 현재 들어가있는 행길이 뒤에 들어가야하므로, 대각선의 차가 그만큼 나야한다.
        # 예를 들어서 현재 (0,0)만 sol 있는 경우에는 다음에 놓일 퀸은 1행에 들어가게 되므로 대각선에 해당하는 값은 (1,1)밖에 없으므로 dist=1
        # 현재 (0,0) (1,2) 가 들어가있는 경우에는 (0,0)에서 확인하는 경우라도 다음에 놓일 퀸은 2행에 들어가게 되므로 대각선에 해당하는 값은 (2,2) 이르모 dist = 2 (len(sol)-i)
        # if sol[i] + dist in candidate: #같은 대각선
        #     candidate.remove(sol[i] + dist)
        if sol[i] - dist in candidate:
            candidate.remove(sol[i] - dist)
        if sol[i] + dist in candidate:
            candidate.remove(sol[i] + dist)
    if candidate:
        for c in candidate:
            sol.append(c)
            bfs(sol,n)
            sol.pop()
    else:
        return

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for i in range(N):
        sol = [i]
        bfs(sol,N)
    print(count)