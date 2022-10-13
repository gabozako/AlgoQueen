# 마법사 상어와 비바라기
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

clouds = ((N-1,0),(N-1,1),(N-2,0),(N-2,1))


drc = [
    [0,-1],
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,1],
    [1,1],
    [1,0],
    [1,-1]
]
dia = [[-1,-1],[-1,1],[1,1],[1,-1]]

def is_valid(i,j):
    if 0<= i <= N-1 and 0<= j <= N-1:
        return True

    return False

def print_board():
    for i in range(N):
        print(board[i])
    print("===========")


def practice(dr, ds):
    # 구름 이동
    new_clouds = tuple(map(lambda x: ((x[0] + drc[dr-1][0] * ds) % N, (x[1] + drc[dr-1][1] * ds) % N), clouds))

    # 비내림
    for ci, cj in new_clouds:
        board[ci][cj] += 1

    # 물복사
    for ci, cj in new_clouds:
        cnt = 0
        for k in range(4):
            ni = ci + dia[k][0]
            nj = cj + dia[k][1]
            if is_valid(ni,nj) and board[ni][nj]:
                cnt += 1
        board[ci][cj] += cnt

    new_new_clouds = []
    # 새로운 구름
    for i in range(N):
        for j in range(N):
            if board[i][j] >=2 and (i,j) not in new_clouds:
                new_new_clouds.append((i,j))
                board[i][j] -= 2

    return tuple(new_new_clouds)



# 명령수행
for _ in range(M):
    dr, ds = map(int, input().split())
    clouds = practice(dr, ds)

answer = 0
for b in board:
    answer += sum(b)

print(answer)
