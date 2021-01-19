import sys
# def L(a,index):
#     if index == 0:
#         pass
#     else:
#         index-=1
#     return index

# def D(a,index):
#     if index == len(a):
#         pass
#     else:
#         index+=1
#     return index

# def B(a,index):
#     if index == 0:
#         pass
#     else:
#         del a[index-1]
#         index-=1
#     return index

# def P(a,index,x):
#     a.insert(index,x)
#     index+=1
#     return index
    
# if __name__ == "__main__":
#     a = list(sys.stdin.readline().rstrip())
#     index = len(a)
#     m = int(sys.stdin.readline().rstrip())
#     command = [sys.stdin.readline().rstrip() for x in range(m)]
#     for c in command:
#         if c.startswith('P'):
#             index = P(a,index,c.split()[1])
#         elif c == 'L':
#             index = L(a,index)
#         elif c == 'D':
#             index = D(a,index)
#         elif c == 'B':
#             index = B(a,index)
#     answer =''
#         answer+=i
#     print(answer)

#두개 리스트 사용 
if __name__ == "__main__":
    left = list(sys.stdin.readline().rstrip())
    right= []
    m = int(sys.stdin.readline().rstrip())
    for i in range(m):
        command = sys.stdin.readline().rstrip().split()
        if command[0]== 'P':
            left.append(command[1])
        elif command[0] == 'L':
            if len(left)!=0:
                right.append(left.pop())
        elif command[0] == 'D':
            if len(right)!=0:
                left.append(right.pop())
        elif command[0] == 'B':
            if len(left)!=0:
                left.pop()
    print(''.join(left+right[::-1]))