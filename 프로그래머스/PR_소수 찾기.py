from itertools import permutations

def solution(numbers):
    answer = set()
    permute = []
    for i in range(1,len(numbers)+1):
        temp = list(permutations(numbers,i))
        permute+=temp
    for i in permute:
        result = ''
        for j in i:
            result+=j
        result = int(result)
        if result==1 or result == 0:
            continue
        else:
            prime = True
            for k in range(2,result):
                if result%k==0:
                    prime = False
                    break
            if prime==True:
                answer.add(result)
    print(len(answer))
    return len(answer)

solution("011")