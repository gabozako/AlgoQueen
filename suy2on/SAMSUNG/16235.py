import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
S2D2 = []
drc = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

def is_valid(i,j):
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        return True
    return False


for _ in range(N):
    S2D2.append(list(map(int, input().split())))

# 모든 칸에 양분 5씩
foods = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

def print_board(board):
    for i in range(N):
        print(board[i])
    print("===========")

# r, c는 1부터시작
for _ in range(M):
    si,sj,age = map(int, input().split())
    trees[si-1][sj-1].append(age)


## 봄 여름
def spring_and_summer():
    # 나이만큼 양분 먹고 나이 증가
    for i in range(N):
        for j in range(N):
            new_tree = []
            trees[i][j].sort(reverse=True)

            # 나이가 어린 나무부터 먹음 -> 못먹은 나무는 죽음
            while trees[i][j]:
                if trees[i][j][-1] > foods[i][j]:
                    break
                foods[i][j] -= trees[i][j][-1]
                new_tree.append(trees[i][j].pop()+1)


            # 죽은 나무는 나이의 2로 나눈 몫 만큼 양분이 된다
            for tree in trees[i][j]:
                foods[i][j] += tree // 2

            trees[i][j] = new_tree

## 가을
def fall():
    # 나이가 5의 배수이면 번식 : 인접 8칸에 나이 1인 나무 추가
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:
                if tree % 5 == 0:
                    for k in range(8):
                        ni = i + drc[k][0]
                        nj = j + drc[k][1]
                        if is_valid(ni,nj):
                            trees[ni][nj].append(1)

## 겨울
def winter():
    # 양분추가
    for i in range(N):
        for j in range(N):
            foods[i][j] += S2D2[i][j]


for _ in range(K):
    spring_and_summer()
    # print("SS")
    # print_board(foods)
    # print_board(trees)
    fall()
    # print("F")
    # print_board(foods)
    # print_board(trees)
    winter()
    # print("W")
    # print_board(foods)
    # print_board(trees)

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)
