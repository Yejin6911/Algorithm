import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    t = [int(sys.stdin.readline().rstrip()) for x in range(T)]
    result = [1,2,4]
    for i in range(3, max(t)):
        result.append(result[i-1]+result[i-2]+result[i-3])

    for i in t:
        print(result[i-1])