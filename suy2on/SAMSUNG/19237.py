## 어른상어
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
remove_shark = 0

def is_valid(i,j):
    if 0<= i <= N-1 and 0 <= j <= N-1:
        return True
    return False

def print_board(board):
    for i in range(N):
        print(board[i])
    print("=======")

for _ in range(N):
    board.append(list(map(int, input().split())))

# 상어들 보고있는 방향
shark_looking_for = list(map(int, input().split()))

# 상하좌우
dir_ord = [[-1,0],[1,0],[0,-1],[0,1]]

# 상어마다 방향에 대한 우선순위
shark_dir_ord = []
for _ in range(M):
    shark_ord = []
    for _ in range(4):
        shark_ord.append(list(map(int, input().split())))

    shark_dir_ord.append(shark_ord)

# 피냄새 초기세팅
blood = [[0] * N for _ in range(N)]
blood_for = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j]:
            blood[i][j] = K
            blood_for[i][j] = board[i][j]


# 이동
def shark_move(si, sj, num, new_board):
    global remove_shark

    look = shark_looking_for[num-1]
    move_ord = shark_dir_ord[num-1][look-1]

    # 1순위 냄새없는칸
    for d in move_ord:
        ni = si + dir_ord[d-1][0]
        nj = sj + dir_ord[d-1][1]
        if is_valid(ni,nj):
            if not blood[ni][nj]:
                # 상어가 없음
                if not new_board[ni][nj]:
                    new_board[ni][nj] = num
                    shark_looking_for[num-1] = d
                # 상어가 있지만 자신보다 덩치 작음
                elif new_board[ni][nj] > num:
                    new_board[ni][nj] = num
                    shark_looking_for[num - 1] = d
                    remove_shark += 1
                # 상어 추방
                else:
                    remove_shark += 1

                return

    # 2순위 자신의 냄새칸
    for d in move_ord:
        ni = si + dir_ord[d - 1][0]
        nj = sj + dir_ord[d - 1][1]
        if is_valid(ni,nj):
            if blood_for[ni][nj] == num:
                # 상어가 없음
                if not new_board[ni][nj]:
                    new_board[ni][nj] = num
                    shark_looking_for[num - 1] = d
                # 상어가 있지만 자신보다 덩치 작음
                elif new_board[ni][nj] > num:
                    new_board[ni][nj] = num
                    shark_looking_for[num - 1] = d
                    remove_shark += 1
                # 상어 추방
                else:
                    remove_shark += 1

                return

    # 움직이지 못함
    if not new_board[si][sj]:
        new_board[si][sj] = num
    elif new_board[si][sj] > num:
        new_board[ni][nj] = num
        remove_shark += 1
    else:
        remove_shark += 1


# 냄새빼고 냄새 남기기
def blood_smell():
    for i in range(N):
        for j in range(N):
            if blood[i][j]:
                blood[i][j] -= 1
                if not blood[i][j]:
                    blood_for[i][j] = 0

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                blood[i][j] = K
                blood_for[i][j] = board[i][j]

finish = False
for sec in range(1000):
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                shark_move(i,j,board[i][j], new_board)

    board = new_board
    # print_board(board)

    if remove_shark == M-1:
        print(sec+1)
        finish = True
        break

    blood_smell()
    # print_board(blood)
    # print_board(blood_for)
    # print("&&&&&&&&&&&")

if not finish:
    print(-1)





