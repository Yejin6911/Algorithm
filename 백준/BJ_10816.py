import sys

#시간초과_이분탐색 사용
def count(target, array):
    start=0
    end = len(array)-1
    count = 0
    
    while start <= end:
        mid = (start+end) //2
        if target == array[mid]:
            count += 1
            i, j = 1,1
            while mid-i >= start:
                if array[mid-i] != target:
                    break
                else:
                    count+= 1
                    i+= 1
            while mid+j <= end:
                if array[mid+j] != target:
                    break
                else: 
                    count += 1 
                    j+=1
            break
        elif array[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return count
        
    
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    A = list(map(int,sys.stdin.readline().rstrip().split()))
    A.sort()
    m = int(sys.stdin.readline().rstrip())
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    result=[]
    for i in B:
        print(count(i,A),end=' ')



#정렬 후 탐색, 딕셔너리 사용
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    A = list(map(int,sys.stdin.readline().rstrip().split()))
    A.sort()
    m = int(sys.stdin.readline().rstrip())
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    result={}
    index = 0
    for b in sorted(B):
        count = 0
        if b not in result:
            while index < len(A):
                if b == A[index]:
                    count+=1
                    index+=1
                elif b > A[index]:
                    index+=1
                else:
                    break
            result[b] = count
         
    for i in B:
        print(result[i], end=' ')

#해시 알고리즘 사용
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    A = list(map(int,sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    result = {}

    for i in A:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    for i in B:
        if i in result:
            print(result[i],end=' ')
        else:
            print(0, end=' ')

