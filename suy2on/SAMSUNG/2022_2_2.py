##예술성
import sys
import collections
import itertools
input = sys.stdin.readline

N = int(input())
board = []
drc = [[1,0],[-1,0],[0,-1],[0,1]]

def is_valid(i,j):
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        return True
    return False

def print_board():
    for i in range(N):
        print(board[i])
    print()

for _ in range(N):
    board.append(list(map(int, input().split())))

# 그룹구하기
def group(si, sj, visited):
    group = [[si,sj]]
    neighber = []
    queue = collections.deque()
    queue.append([si,sj])
    visited[si][sj] = True

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + drc[k][0]
            nj = j + drc[k][1]
            if is_valid(ni,nj):
                # 자신 그룹
                if not visited[ni][nj] and board[si][sj] == board[ni][nj]:
                    queue.append([ni,nj])
                    visited[ni][nj] = True
                    group.append([ni,nj])
                # 다른 것과 접촉
                else:
                    neighber.append([ni,nj])

    return [board[si][sj], group, neighber]


# 예술성계산
def compute_score():
    # 그룹찾기
    groups = []
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                groups.append(group(i,j,visited))

    # TODO : 그룹별로 숫자가 같을 수도 있어서 그룹 인덱스로해서 주변 블록들 in연산으로 어떤 그룹소속인지 찾아야함
    # 그룹별 이웃구하기
    for g in groups:
        neighber = collections.defaultdict(int)
        for n in g[2]:
            for i in range(len(groups)):
                if n in groups[i][1]:
                    neighber[i] += 1
                    break
        g[2] = neighber


    # 그룹별로 조화로움 구하기
    score = 0
    for one, two in itertools.combinations(range(len(groups)), 2):
        num1, many1, nei1 = groups[one]
        num2, many2, nei2 = groups[two]
        score += (len(many2) + len(many1)) * num1 * num2 * nei1[two]


    return score

# 회전
def turn90():
    new_board = [[0] * N for _ in range(N)]
    mid = N // 2

    # 십자가
    for i in range(N):
        new_board[mid][i] = board[i][mid]
        new_board[N-1-i][mid] = board[mid][i]

    # 양끝 네모들
    si, sj = 0, 0
    for i in range(N//2):
        for j in range(N//2):
            new_board[si+i][sj+j] = board[si+(N//2)-1-j][sj+i]

    si, sj = 0, N//2+1
    for i in range(N // 2):
        for j in range(N // 2):
            new_board[si + i][sj + j] = board[si + (N // 2) - 1 - j][sj + i]

    si, sj = N//2+1, 0
    for i in range(N // 2):
        for j in range(N // 2):
            new_board[si + i][sj + j] = board[si + (N // 2) -1 - j][sj + i]

    si, sj = N//2+1, N//2+1
    for i in range(N // 2):
        for j in range(N // 2):
            new_board[si + i][sj + j] = board[si + (N // 2) -1 - j][sj + i]


    return new_board


answer = 0
# print_board()
answer += compute_score()
board = turn90()
# print_board()
answer += compute_score()
board = turn90()
# print_board()

answer += compute_score()
board = turn90()
# print_board()

answer += compute_score()

print(answer)








