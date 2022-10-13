## 꼬리잡기
import sys
import collections
input = sys.stdin.readline

N, M, K = map(int, input().split())
drc = [[0,1], [0,-1], [1,0], [-1,0]]
# 공 던져지는
ball_dir = [[0,1],[-1,0],[0,-1],[1,0]]

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def is_valid(i,j):
    if 0 <= i <= N-1 and 0<= j <= N-1 and board[i][j] != 0:
        return True
    return False

def print_board():
    for i in range(N):
        print(board[i])
    print()

## 머리따라 움직이기
def move():
    new_board = [[0] * N for _ in range(N)]

    # 1 -> 4 / 2 -> 1 / 2 -> 2/ 3 -> 2
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                for k in range(4):
                    ni = i + drc[k][0]
                    nj = j + drc[k][1]
                    if is_valid(ni, nj) and (board[ni][nj] == 4 or board[ni][nj] == 3):
                        new_board[ni][nj] = 1
                        break

            elif board[i][j] == 2:
                for k in range(4):
                    ni = i + drc[k][0]
                    nj = j + drc[k][1]
                    if is_valid(ni, nj):
                        if board[ni][nj] == 2 and not new_board[ni][nj]:
                            new_board[ni][nj] = 2
                        elif board[ni][nj] == 1:
                            new_board[ni][nj] = 2

            elif board[i][j] == 3:
                for k in range(4):
                    ni = i + drc[k][0]
                    nj = j + drc[k][1]
                    if is_valid(ni, nj) and board[ni][nj] == 2:
                        new_board[ni][nj] = 3
                        if not new_board[i][j]:
                            new_board[i][j] = 4
                        break

            elif board[i][j] == 4:
                if not new_board[i][j]:
                    new_board[i][j] = 4

    return new_board

## start에서 end까지 거리구하기
def bfs(start,end):
    queue = collections.deque()
    queue.append([start[0], start[1], 0])
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True

    while queue:
        i, j, c = queue.popleft()

        if board[i][j] == end:
            return [i,j,c+1]

        for k in range(4):
            ni = i + drc[k][0]
            nj = j + drc[k][1]
            if is_valid(ni,nj):
                if board[ni][nj] != 2:
                    if board[i][j] == 2 and board[ni][nj] == end:
                        return [ni,nj,c+2]
                else:
                    if not visited[ni][nj]:
                        visited[ni][nj] = True
                        queue.append([ni,nj,c+1])

    return [0,0,0]


## 공을 최초로 맞은 사람 찾고 점수 추가
def hit_ball(round):

    round = round % (4*N)
    d = round // N
    m = round % N

    # 공던지는 시작점
    if d == 0:
        si, sj = m, 0
    elif d == 1:
        si, sj = N-1, m
    elif d == 2:
        si, sj = N-1-m, N-1
    else:
        si, sj = 0, N-1-m

    # print(si,sj,ball_dir[d])
    # 사람 만날때 까지
    while 0 <= si <= N-1 and 0 <= sj <= N-1 and (board[si][sj] == 4 or board[si][sj] == 0):
        si += ball_dir[d][0]
        sj += ball_dir[d][1]

    # 중간에 맞은 사람 있으면 머리찾고 꼬리머리 바꾸기
    # print(si,sj)
    if 0 <= si <= N-1 and 0 <= sj <= N-1:
        hi, hj, score = bfs([si,sj],1)
        # print(hi,hj)
        ti, tj, cost = bfs([hi,hj], 3)
        board[ti][tj] = 1
        board[hi][hj] = 3
        # print(ti,tj)
        return score ** 2

    return 0



answer = 0
for r in range(K):
     board = move()
     # print_board()
     s = hit_ball(r)
     # print_board()
     answer += s
     # print(answer)
     # print("%%%%%%")

print(answer)





