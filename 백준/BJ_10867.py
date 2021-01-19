import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    A = list(map(int,sys.stdin.readline().rstrip().split()))
    set_A = set(A)
    A = list(set_A)
    A.sort()
    for i in A:
        print(i,end=' ')