## 나무의 박멸
import sys
input = sys.stdin.readline

N, M, K, C = map(int, input().split())

drc = [[1,0],[-1,0],[0,1],[0,-1]]
board = []
spray = [[0] * N for _ in range(N)]
for _ in range(N):
    board.append(list(map(int, input().split())))


def is_valid(i,j):
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        return True
    return False

def print_board(board):
    for i in range(N):
        print(board[i])
    print()


## 성장
def grow():
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                age = 0
                for k in range(4):
                    ni = i + drc[k][0]
                    nj = j + drc[k][1]
                    if is_valid(ni,nj) and board[ni][nj]>0:
                        age += 1

                board[i][j] += age
## 번식
def breed():
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[i][j] += board[i][j]
            if board[i][j] > 0:
                can_breed = []
                for k in range(4):
                    ni = i + drc[k][0]
                    nj = j + drc[k][1]
                    if is_valid(ni,nj) and board[ni][nj] == 0 and not spray[ni][nj]:
                        can_breed.append([ni,nj])
                # 번식
                if can_breed:
                    b = board[i][j] // len(can_breed)
                    for ni, nj in can_breed:
                        new_board[ni][nj] += b

    return new_board

ddrc = [[1,1],[-1,-1],[1,-1],[-1,1]]

## 제초제 뿌릴 때 죽는 나무
def how_many_tree_is_dead(i,j):
    cnt = board[i][j]
    for k in range(4):
        pi = i
        pj = j
        for _ in range(K):
            pi += ddrc[k][0]
            pj += ddrc[k][1]
            if is_valid(pi,pj):
                if board[pi][pj] == -1 or board[pi][pj] == 0:
                    break
                cnt += board[pi][pj]

    return cnt





## 제초제 날리고 제초시작
def kill_tree():
    for i in range(N):
        for j in range(N):
            if spray[i][j]:
                spray[i][j] -= 1


    # 죽일 나무 찾기
    can_kill_tree = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 or board[i][j] == -1:
                can_kill_tree.append([0,i,j])
            else:
                cnt = how_many_tree_is_dead(i,j)
                can_kill_tree.append([cnt,i,j])

    can_kill_tree.sort(key=lambda x : (-x[0], x[1], x[2]))
    cnt, si, sj = can_kill_tree[0]

    # 제초제 뿌리기
    spray[si][sj] = C
    if cnt:
        board[si][sj] = 0

        for k in range(4):
            pi = si
            pj = sj
            for _ in range(K):
                pi += ddrc[k][0]
                pj += ddrc[k][1]
                if is_valid(pi, pj):
                    spray[pi][pj] = C
                    if board[pi][pj] == -1 or board[pi][pj] == 0:
                        break
                    board[pi][pj] = 0

    return cnt

answer = 0
for _ in range(M):
    grow()
    # print_board(board)
    board = breed()
    # print_board(board)
    answer += kill_tree()
    # print_board(board)
    # print_board(spray)
    #
    # print("*******")



print(answer)



