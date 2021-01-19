import sys

def b_search(target,data):
    start = 0
    end = len(data) - 1
    
    while start <= end:
        mid = (start+end) // 2
        if target == data[mid]:
            return 1
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    list_n = list(map(int, sys.stdin.readline().rstrip().split()))
    list_n.sort()
    m = int(sys.stdin.readline().rstrip())
    list_m = list(map(int, sys.stdin.readline().rstrip().split()))
    
    for i in list_m:
        print(b_search(i,list_n), end=' ') 
