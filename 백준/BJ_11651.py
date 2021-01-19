import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    A = []
    for i in range(n):
        A.append(list(map(int,sys.stdin.readline().rstrip().split())))
    A= sorted(A, key=lambda x: (x[1], x[0]))
    for i in A:
        print(str(i[0])+' '+str(i[1]))

