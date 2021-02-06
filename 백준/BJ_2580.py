import sys


def check(x, y, val):
    # 가로 확인
    if val in S[x]:
        return False
    # 세로 확인
    for i in range(9):
        if val == S[i][y]:
            return False
    # 3X3 안의 수 확인
    row = x//3 * 3
    col = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == S[row+i][col+j]:
                return False
    return True


def DFS(index, blanks):
    # 전체 다 채워졌을 때 출력
    if index == len(blanks):
        for row in S:
            for col in row:
                print(col, end=' ')
            print()
        # 종료
        sys.exit()
    else:
        x = blanks[index][0]
        y = blanks[index][1]

        # 넣으려는 숫자 i
        for i in range(1, 10):
            if check(x, y, i):
                S[x][y] = i
                DFS(index+1, blanks)
                # 다음 숫자 가능 여부 판단을 위해 다시 0으로 돌려놓기
                S[x][y] = 0


if __name__ == "__main__":
    S = [list(map(int, sys.stdin.readline().rstrip().split()))
         for x in range(9)]
    blanks = []
    for i in range(9):
        for j in range(9):
            if S[i][j] == 0:
                blanks.append((i, j))
    DFS(0, blanks)
