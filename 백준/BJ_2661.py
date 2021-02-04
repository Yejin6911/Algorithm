import sys


def back_tracking(answer, idx):
    # 중복되는 부분수열이 있는지 확인
    for i in range(1, (idx//2)+1):
        if answer[-i:] == answer[-2*i:-i]:
            return
    # 정답을 찾았을 경우
    if idx == N:
        print(int(answer))
        exit()

    for i in ['1', '2', '3']:
        back_tracking(answer+i, idx+1)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    answer = '1'
    back_tracking(answer, 1)
