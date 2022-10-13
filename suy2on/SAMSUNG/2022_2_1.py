## 술래잡기
import sys

input = sys.stdin.readline

N, M, H, K = map(int, input().split())

board = [[[] for _ in range(N)] for _ in range(N)]
trees = [[False] * N for _ in range(N)]
runner_dir = [[[0, 1], [0, -1]], [[1, 0], [-1, 0]]]

for _ in range(M):
    i, j, d = map(lambda x: int(x) - 1, input().split())
    board[i][j].append([d, 0])

for _ in range(H):
    i, j = map(lambda x: int(x) - 1, input().split())
    trees[i][j] = True

ci, cj = N//2, N//2

def is_valid(i,j):
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        return True
    return False

def print_board(board):
    for i in range(N):
        print(board[i])
    print()

# 도망자 이동
def runner_move():
    new_board = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                distance = abs(ci-i) + abs(cj - j)
                # 거리 3 이하면
                if distance <= 3:
                    for d, look in board[i][j]:
                        rd = runner_dir[d][look]
                        ni = i + rd[0]
                        nj = j + rd[1]
                        if is_valid(ni,nj):
                            # 술래없다면
                            if [ni,nj] != [ci,cj]:
                                new_board[ni][nj].append([d,look])
                            # 술래있다면
                            else:
                                new_board[i][j].append([d,look])
                        else:
                            # 방향바꾸기
                            rd = runner_dir[d][1 ^ look]
                            ni = i + rd[0]
                            nj = j + rd[1]
                            # 술래없다면
                            if [ni, nj] != [ci, cj]:
                                new_board[ni][nj].append([d, 1 ^ look])
                            # 술래있다면
                            else:
                                new_board[i][j].append([d, 1 ^ look])

                # 거리 3 초과
                # TODO : 거리 초과하는 곳이여도 위에서 이동한 애들이 들어있을 수 있기때문에 extend로 확장만해줘야함 대체해버리면 걔들 없어짐
                else:
                    new_board[i][j].extend(board[i][j])


    return new_board

modes = [[[-1,0],[0,1],[1,0],[0,-1]], [[0,1],[-1,0],[0,-1],[1,0]]]
def where_to_move(k):
    nk = k % (((N * (N - 1)) + (N - 1)) * 2)
    mode = nk // ((N * (N - 1)) + (N - 1))
    p = nk % ((N * (N - 1)) + (N - 1))
    # 감아지는
    # print(mode, p)
    if mode == 0:
        # extra : 위
        if p >= (N * (N-1)):
            return [-1,0]
        # 소용돌이
        else:
            cnt = 0
            for i in range(2*(N-1)):
                loop = i // 2 + 1
                d = i%4
                cnt += loop
                if cnt > p:
                    return modes[mode][d]

    # 풀어지는
    else:
        # extra : 아래
        if p < N-1:
            return [1, 0]
        # 소용돌이
        else:
            cnt = N-1
            for i in range(2 * (N - 1)):
                loop = N - (i // 2 + 1)
                d = i % 4
                cnt += loop
                if cnt > p:
                    return modes[mode][d]





# 술래이동
def move_catcher(k):
    global ci, cj

    d = where_to_move(k)
    # print(d)
    ci += d[0]
    cj += d[1]
    # 다음 방향 기준으로 잡기 -> 바뀔수도 있으니까
    d = where_to_move(k+1)
    # print(d)
    # print(ci,cj)

    # 도망자 잡기 + 점수획득
    score = 0
    pi, pj = ci, cj
    if not trees[pi][pj]:
        score += (len(board[pi][pj]) * (k + 1))
        board[pi][pj].clear()
    for _ in range(2):
        pi += d[0]
        pj += d[1]
        if is_valid(pi,pj):
            if trees[pi][pj]:
                continue
            score += (len(board[pi][pj]) * (k+1))
            board[pi][pj].clear()
        else:
            break


    return score


answer = 0
# print_board(board)
# print_board(trees)

for r in range(K):
    print_board(board)
    board = runner_move()
    print_board(board)
    answer += move_catcher(r)
    print(ci,cj)
    print_board(board)
    print("&&&&&&&")

print(answer)
