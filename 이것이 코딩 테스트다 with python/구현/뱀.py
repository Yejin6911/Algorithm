import sys

n = int(sys.stdin.readline().rstrip())
B = [[0]*n for _ in range(n)]
k = int(sys.stdin.readline().rstrip())
# 사과 있는 곳은 1로 update
for i in range(k):
    row, col = map(int, sys.stdin.readline().rstrip().split())
    B[row-1][col-1] = 1

l = int(sys.stdin.readline().rstrip())

# 방향을 바꿔줘야 하는 시간과 방향을 딕셔너리 형태로 저장
turn = {}
for i in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    turn[int(x)] = c

result = 0

# 방향에 따른 좌표 이동 (0:동, 1:서, 2:남, 3:북)
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
now_d = 0
now = [(0, 0)]  # 뱀이 차지하는 보드의 좌표들
# 뱀 머리 위치
now_row = 0
now_col = 0

while True:
    result += 1
    new_row = now_row + direction[now_d][0]
    new_col = now_col + direction[now_d][1]
    # 보드판을 벗어나거나 자기 자신을 만난 경우 반복문 탈출
    if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n or (new_row, new_col) in now:
        break
        # 사과를 만난 경우
    if B[new_row][new_col] == 1:
        now.append((new_row, new_col))
        now_row = new_row
        now_col = new_col
        B[new_row][new_col] = 0
        # 사과가 아닌 경우
    else:
        now.pop(0)
        now.append((new_row, new_col))
        now_row = new_row
        now_col = new_col
    # 방향 바꿔야 하는지 확인
    if result in turn.keys():
        if turn[result] == 'L':  # 왼쪽
            now_d = ((now_d-1)+4) % 4
        elif turn[result] == 'D':  # 오른쪽
            now_d = (now_d+1) % 4

print(result)
