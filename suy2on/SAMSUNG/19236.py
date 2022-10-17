## 청소년상어
import sys
import collections
import copy

input = sys.stdin.readline
drc = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

board = []
fishes = {}
for _ in range(4):
    fishs = []
    fish = list(map(int, input().split()))
    for i in range(0,8,2):
        ## TODO : 방향은 0부터 시작하게
        fishs.append([fish[i],fish[i+1]-1])
    board.append(fishs)

# 물고기 변호별 위치
for i in range(4):
    for j in range(4):
        fishes[board[i][j][0]] = [i,j]


def is_valid(i,j):
    if 0 <= i <= 3 and 0 <= j <= 3:
        return True
    return False

## 물고기이동
def fish_move(fs, bd, si, sj):
    for f in sorted(fs.keys()):
        i, j = fs[f]
        # print(f, i, j)
        d = bd[i][j][1]
        for k in range(8):
            ni = i + drc[(d+k)%8][0]
            nj = j + drc[(d+k)%8][1]
            if is_valid(ni,nj):
                # 빈칸에 상어없음
                if not bd[ni][nj]:
                    if [si,sj] != [ni,nj]:
                        bd[i][j].clear()
                        bd[ni][nj] = [f,(d+k)%8]
                        fs[f] = [ni,nj]
                        # print(ni,nj)
                        break
                # 다른 물고기 있음
                else:
                    bd[i][j][1] = (d+k)%8
                    bd[i][j], bd[ni][nj] = bd[ni][nj], bd[i][j]
                    fs[f] = [ni,nj]
                    fs[bd[i][j][0]] = [i,j]
                    # print(ni,nj)
                    break




shark = [0,0,board[0][0][1]]
fish_num = board[0][0][0]
del fishes[fish_num]

board[0][0].clear()
queue = collections.deque()
queue.append([fish_num, shark, board, fishes])

answer = -1

while queue:
    sum_num, shk, bd, fs = queue.popleft()

    si, sj, sd = shk

    fish_move(fs, bd, si, sj)


    # 상어이동
    ni = si
    nj = sj
    mv = 0
    while True:
        ni += drc[sd][0]
        nj += drc[sd][1]
        if is_valid(ni,nj):
            # 물고기 있으면 먹기
            if bd[ni][nj]:
                cbd = copy.deepcopy(bd)
                cfs = copy.deepcopy(fs)
                num, fd = cbd[ni][nj]
                nshk = [ni,nj,fd]
                del cfs[num]
                cbd[ni][nj].clear()
                queue.append([sum_num+num, nshk, cbd, cfs])
                mv += 1
            ## TODO : 물고기 있어도 이동가능

        # 더이상 이동 불가
        else:
            break

    # 이동못했으면
    if not mv:
        answer = max(answer, sum_num)


print(answer)