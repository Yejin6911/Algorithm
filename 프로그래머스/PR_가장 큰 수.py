#방법 1
def solution(numbers):
    numbers = list(map(str, numbers))
    #천 이하의 세자리를 일의자리까지 비교하기 위해 세번 곱해준다. ex) 9, 91, 912 중 더 앞에 와야 하는 것을 찾을 때.
    numbers.sort(key=lambda x: x * 3, reverse=True)
    answer = ''
    if sum(list(map(int,numbers)))==0:
        return '0'
    else:
        for num in numbers:
            answer+=num
        return answer


#방법 2
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([3, 30, 34, 5, 9]))