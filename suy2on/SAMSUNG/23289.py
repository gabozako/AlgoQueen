## 온풍기 안녕
import sys
import collections
import copy

input = sys.stdin.readline

R, C, K = map(int, input().split())
room = []
heat = [[0] * C for _ in range(R)]

walls = collections.defaultdict(list)
warmmer = []

for _ in range(R):
    room.append(list(map(int, input().split())))

W = int(input())

# 벽추가
for _ in range(W):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    if d == 0:
        walls[(r, c)].append([r - 1, c])
        walls[(r - 1, c)].append([r, c])

    else:
        walls[(r, c)].append([r, c + 1])
        walls[(r, c + 1)].append([r, c])



def is_valid(i, j):
    if 0 <= i <= R - 1 and 0 <= j <= C - 1:
        return True
    return False


# 오른 왼 위 아래
drc = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# 조사해야하는 칸
looks = []
for i in range(R):
    for j in range(C):
        if room[i][j] == 5:
            looks.append([i, j])


# 온풍기조사
for i in range(R):
    for j in range(C):
        if 1 <= room[i][j] <= 4:
            warmmer.append([i, j])



# 벽여부
def is_wall(i1,j1,i2,j2):
    if [i2,j2] in walls[(i1,j1)]:
        return True
    return False


## 바람나옴
def warming(si,sj):
    new_heat = [[0] * C for _ in range(R)]
    d = room[si][sj] - 1

    # 오른쪽
    if d == 0:
        if is_valid(si+drc[d][0], sj+drc[d][1]):
            new_heat[si+drc[d][0]][sj+drc[d][1]] += 5
        move = [[0,1],[-1,1],[1,1]]
        for i in range(1,5):
            for j in range(i):
                # 위쪽
                ni = si + j
                nj = sj + i
                if is_valid(ni,nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni+m[0],nj) and not is_wall(ni,nj,ni+m[0],nj) and is_valid(ni+m[0], nj+m[1]) and not is_wall(ni+m[0],nj, ni+m[0], nj+m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5-i

                # 아래쪽
                ni = si - j
                nj = sj + i
                if is_valid(ni, nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni + m[0], nj) and not is_wall(ni, nj, ni + m[0], nj) and is_valid(ni + m[0], nj + m[1]) and not is_wall(ni + m[0], nj, ni + m[0], nj + m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5 - i


    # 왼쪽
    elif d == 1:
        if is_valid(si + drc[d][0], sj + drc[d][1]):
            new_heat[si + drc[d][0]][sj + drc[d][1]] += 5
        move = [[0, -1], [-1, -1], [1, -1]]
        for i in range(1, 5):
            for j in range(i):
                # 위쪽
                ni = si + j
                nj = sj - i
                if is_valid(ni, nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni+m[0], nj) and not is_wall(ni, nj, ni + m[0], nj) and is_valid(ni + m[0], nj + m[1]) and not is_wall( ni + m[0], nj, ni + m[0], nj + m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5 - i

                # 아래쪽
                ni = si - j
                nj = sj - i
                if is_valid(ni, nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni + m[0], nj) and not is_wall(ni, nj, ni + m[0], nj) and is_valid(ni + m[0], nj + m[1]) and not is_wall(ni + m[0], nj, ni + m[0], nj + m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5 - i

    # 위
    elif d == 2:
        if is_valid(si + drc[d][0], sj + drc[d][1]):
            new_heat[si + drc[d][0]][sj + drc[d][1]] += 5
        move = [[-1, 0], [-1, -1], [-1, 1]]
        for i in range(1, 5):
            for j in range(i):
                # 왼쪽
                ni = si - i
                nj = sj - j
                if is_valid(ni, nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni, nj+m[1]) and not is_wall(ni, nj, ni, nj+m[1]) and is_valid(ni + m[0], nj + m[1]) and not is_wall(ni, nj+m[1], ni + m[0], nj + m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5 - i

                # 아래쪽
                ni = si - i
                nj = sj + j
                if is_valid(ni, nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni, nj+m[1]) and not is_wall(ni, nj, ni, nj+m[1]) and is_valid(ni + m[0], nj + m[1]) and not is_wall(ni, nj+m[1], ni + m[0], nj + m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5 - i

    # 아래
    elif d == 3:
        if is_valid(si + drc[d][0], sj + drc[d][1]):
            new_heat[si + drc[d][0]][sj + drc[d][1]] += 5
        move = [[1, 0], [1, -1], [1, 1]]
        for i in range(1, 5):
            for j in range(i):
                # 왼쪽
                ni = si + i
                nj = sj - j
                if is_valid(ni, nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni, nj + m[1]) and not is_wall(ni, nj, ni, nj + m[1]) and is_valid(ni + m[0], nj + m[1]) and not is_wall(ni, nj + m[1], ni + m[0], nj + m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5 - i

                # 오른쪽
                ni = si + i
                nj = sj + j
                if is_valid(ni, nj) and new_heat[ni][nj]:
                    for m in move:
                        # 벽이 없어야
                        if is_valid(ni, nj + m[1]) and not is_wall(ni, nj, ni, nj + m[1]) and is_valid(ni + m[0], nj + m[1]) and not is_wall(ni, nj + m[1], ni + m[0], nj + m[1]):
                            nni = ni + m[0]
                            nnj = nj + m[1]
                            if not new_heat[nni][nnj]:
                                new_heat[nni][nnj] += 5 - i

    return new_heat

## 온도조절
ddrc = [[0,1],[1,0]]
def adjust():
    new_heat = copy.deepcopy(heat)


    for i in range(R):
        for j in range(C):
            for k in range(2):
                ni = i + ddrc[k][0]
                nj = j + ddrc[k][1]
                if is_valid(ni,nj) and not is_wall(i,j,ni,nj):
                    dt = abs(heat[ni][nj] - heat[i][j]) // 4
                    if heat[ni][nj] > heat[i][j]:
                        new_heat[ni][nj] -= dt
                        new_heat[i][j] += dt
                    else:
                        new_heat[ni][nj] += dt
                        new_heat[i][j] -= dt

    return new_heat





## 온도 검사
def check_temp():
    for i, j in looks:
        if heat[i][j] < K:
            return False
    return True


choco = 0
# print(walls)
while True:
    ## 온풍기 가동
    for w in warmmer:
        new_heat = warming(w[0],w[1])
        for i in range(R):
            for j in range(C):
                heat[i][j] += new_heat[i][j]


    # for i in range(R):
    #     print(heat[i])
    #
    # print()

    ## 온도조절
    heat = adjust()

    ## 온도감소
    for j in range(C):
        heat[0][j] = max(heat[0][j]-1, 0)
        heat[-1][j] = max(heat[-1][j]-1, 0)

    # for i in range(R):
    #     print(heat[i])
    #
    # print()

    for i in range(1,R-1):
        heat[i][0] = max(heat[i][0]-1, 0)
        heat[i][-1] = max(heat[i][-1]-1, 0)

    # for i in range(R):
    #     print(heat[i])
    #
    # print()


    # 초코먹기
    choco += 1

    if choco >= 100:
        choco += 1
        break


    if check_temp():
        break

print(choco)


