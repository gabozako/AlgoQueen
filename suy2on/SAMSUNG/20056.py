## 마상파
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
drc = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]

board = [[[] for _ in range(N)] for _ in range(N)]


for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m,s,d])

## 이동
def move_fireball():
    new_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for m, s, d in board[i][j]:
                ni = i + drc[d][0] * s
                nj = j + drc[d][1] * s
                ## TODO : 원형으로 연결되어있음
                new_board[ni%N][nj%N].append([m,s,d])

    return new_board


## 두개이상 파볼 칸 조정
def adjust_fireball():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                sum_m = sum([b[0] for b in board[i][j]])
                new_m = sum_m // 5

                sum_s = sum([b[1] for b in board[i][j]])
                new_s = sum_s // len(board[i][j])

                d_type = [0,0]
                for d in [b[2] for b in board[i][j]]:
                    d_type[d%2] += 1

                n = len(board[i][j])
                board[i][j].clear()
                if new_m:
                    if d_type[0] == n or d_type[1] == n:
                        board[i][j].append([new_m, new_s, 0])
                        board[i][j].append([new_m, new_s, 2])
                        board[i][j].append([new_m, new_s, 4])
                        board[i][j].append([new_m, new_s, 6])
                    else:
                        board[i][j].append([new_m, new_s, 1])
                        board[i][j].append([new_m, new_s, 3])
                        board[i][j].append([new_m, new_s, 5])
                        board[i][j].append([new_m, new_s, 7])





for _ in range(K):
    board = move_fireball()
    adjust_fireball()


answer = 0
for i in range(N):
    for j in range(N):
        answer += sum([b[0] for b in board[i][j]])



print(answer)




