## 상어중학교
import sys
import collections

input = sys.stdin.readline

board = []
N, M = map(int, input().split())
for _ in range(N):
    board.append(list(map(int, input().split())))

drc = [[-1,0],[1,0],[0,1],[0,-1]]

def is_valid(i,j):
    if 0<= i <= N-1 and 0<= j <= N-1:
        return True

    return False

def print_board():
    for i in range(N):
        print(board[i])
    print("=====")

# 블록그룹찾기(기준블록도 같이)
def find_block_group(si,sj,visited):
    group = [[si,sj]]
    queue = collections.deque()
    queue.append([si,sj])
    visited[si][sj] = True
    standard = board[si][sj]
    rainbow = 0


    while queue:
        i, j = queue.popleft()
        for k in range(4):
            ni = i + drc[k][0]
            nj = j + drc[k][1]
            # 블럭이 그룹에 포함될 수 있는지
            if is_valid(ni,nj) and not visited[ni][nj]:
                if not board[ni][nj] or board[ni][nj] == standard:
                    group.append([ni,nj])
                    queue.append([ni,nj])
                    visited[ni][nj] = True
                    if not board[ni][nj]:
                        rainbow += 1

    # 무지개 visited 해제 : 모든 그룹에서 공유 가능
    for gi,gj in group:
        if not board[gi][gj]:
            visited[gi][gj] = False

    return [len(group), rainbow, si, sj, group]


# 가장 큰 블록그룹 찾기
def find_max_block_group():
    result = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if 1 <= board[i][j] <= M and not visited[i][j]:
                group = find_block_group(i,j,visited)
                if len(group[4]) == 1:
                    continue
                result.append(group)
    if not result:
        return None
    else:
        return sorted(result, key=lambda x : (-x[0], -x[1], -x[2], -x[3]))[0][4]

score = 0
# 모두 삭제하고 점수 더하기
def delete_group(group):
    global score
    score += len(group) ** 2
    for i, j in group:
        board[i][j] = -3


# 중력작용
def gravity():
    for j in range(N):
        for i in range(N-2, -1, -1):
            if board[i][j] == -1:
                continue
            p = i
            # 빈공간 있으면 내려가기
            while p+1 < N and board[p+1][j] == -3:
                board[p][j], board[p+1][j] = board[p+1][j], board[p][j]
                p += 1

# 반시계 90도 회전
def turn_90():
    new_board = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[i][j] = board[j][N-1-i]

    return new_board


while True:
    group = find_max_block_group()
    if not group:
        break
    delete_group(group)
    gravity()
    board = turn_90()
    gravity()

print(score)


