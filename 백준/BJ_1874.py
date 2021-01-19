import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    a=[int(sys.stdin.readline().rstrip()) for x in range(n)]
    now=1
    stack=[]
    result = []
    temp = True
    for i in a:
        while now <= i:
            stack.append(now)
            result.append('+')
            now+=1
        if stack[-1] == i:
            stack.pop()
            result.append('-')
        else:
            temp = False
            break
    if temp == False:
        print('NO')
    else:
        for i in result:
            print(i)
        
                    
        


