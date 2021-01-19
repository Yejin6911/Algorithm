import sys

# #시간초과
# def AC(P,A):
#     for p in P:
#         if p == 'R':
#             A = list(reversed(A))
#         else:
#             if len(A):
#                 A.pop(0)
#             else:
#                 return 'error'
#     return A

def AC(P,A):
    reverse = False
    for p in P:
        #Reverse일때 마다 바꿔줘서 시간 초과. 변수 선언해 마지막에만 바꿔줄 수 있도록 변경
        if p == 'R':
            reverse = not reverse
        else:
            if len(A):
                if not reverse:
                    A.pop(0)
                else:
                    A.pop(-1)
            else:
                return 'error'
    #이것때매 계속 틀림. 띄어쓰기 있으면 안돼서 이렇게 설정해주어야 함
    if reverse:
        return '['+','.join(list(reversed(A)))+']'
    else:
        return '['+','.join(A)+']'

if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    result = []
    for i in range(t):
        P = list(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        A = sys.stdin.readline().rstrip()[1:-1].split(',')
        if n==0:
            A = []
        result.append(AC(P,A))
    for r in result:
        print(r)

