## 주사위 굴리기
import sys
import collections
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
# 우하상좌 : 홀수는 가로 짝수는 세로
drc = [[0,1],[1,0],[0,-1],[-1,0]]

# 처음 방향은 오른쪽
d = 0
ci, cj = 0,0
dice = [
    [0,2,0],
    [4,1,3],
    [0,5,0],
    [0,6,0]
]

for _ in range(N):
    board.append(list(map(int, input().split())))

def is_valid(i,j):
    if 0 <= i <= N-1 and 0 <= j <= M-1:
        return True
    return False

def print_dice():
    for i in range(4):
        print(dice[i])
    print()

## 주사위 이동
def move_dice():
    global ci, cj, d

    ni = ci + drc[d][0]
    nj = cj + drc[d][1]
    if is_valid(ni,nj):
        ci, cj = ni, nj
    # 방향바꾸기
    else:
        d = (d - 2) % 4
        ni = ci + drc[d][0]
        nj = cj + drc[d][1]
        ci, cj = ni, nj

    # print(ci,cj)
    # 주사위 배치변경
    new_dice = [[0] * 3 for _ in range(4)]
    if d % 2 == 1: # 위아래로 이동
        for i in range(4):
            new_dice[(i + drc[d][0]) % 4][1] = dice[i][1]

    else: # 좌우로 이동
        if d == 0: # 우
            new_dice[1][2] = dice[1][1]
            new_dice[1][1] = dice[1][0]
            new_dice[1][0] = dice[3][1]
            new_dice[3][1] = dice[1][2]
        else: # 좌
            new_dice[1][2] = dice[3][1]
            new_dice[1][1] = dice[1][2]
            new_dice[1][0] = dice[1][1]
            new_dice[3][1] = dice[1][0]


    for i in range(4):
        for j in range(3):
            if not new_dice[i][j]:
                new_dice[i][j] = dice[i][j]


    return new_dice

## 점수획득
def add_score():
    B = board[ci][cj]

    C = 1
    visited = [[False] * M for _ in range(N)]
    queue = collections.deque()
    queue.append([ci,cj])
    visited[ci][cj] = True

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + drc[k][0]
            nj = j + drc[k][1]
            if is_valid(ni,nj) and not visited[ni][nj]:
                visited[ni][nj] = True
                if board[ni][nj] == board[i][j]:
                    C += 1
                    visited[ni][nj] = True
                    queue.append([ni,nj])

    return B * C

## 이동방향결정
def next_direction():
    B = board[ci][cj]
    A = dice[3][1]

    if A > B:
        return (d + 1) % 4
    elif A < B:
        return (d - 1) % 4
    else:
        return d

answer = 0
for _ in range(K):
    dice = move_dice()
    # print_dice()
    answer += add_score()
    d = next_direction()



print(answer)