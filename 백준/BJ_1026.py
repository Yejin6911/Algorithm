import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    A = map(int,sys.stdin.readline().rstrip().split())
    B = map(int,sys.stdin.readline().rstrip().split())
    B_sorted = sorted(B)
    A_sorted = sorted(A, reverse=True)
    result = 0
    for i in range(n):
        result += B_sorted[i]*A_sorted[i]
    print(result)