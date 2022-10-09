import sys

input = sys.stdin.readline

# 물고기이동 화살표
fish_dxy = {
    1 : [0,-1],
    2 : [-1,-1],
    3 : [-1,0],
    4 : [-1,1],
    5 : [0,1],
    6 : [1,1],
    7 : [1,0],
    8 : [1,-1]
}

# 상 좌 하 우
shark_dxy = [[-1,0], [0,-1], [1,0], [0,1]]
fishbowl = [[[] for _ in range(4)] for _ in range(4)]

M, S = map(int, input().split())

# 처음 물고기 기록
for _ in range(M):
    r, c, d = map(int, input().split())
    fishbowl[r-1][c-1].append(d)



# 상어기록
si, sj = map(int, input().split())
si -= 1
sj -= 1


# 피냄새 기록
blood_smell =[[0] * 4 for _ in range(4)]



# 물고기가 움직일 수 있는지
def is_fish_valid(i,j):
    if not (0 <= i <= 3 and 0 <= j <= 3):
        # print("range")
        return False
    if blood_smell[i][j]:
        # print("blood")
        return False
    if i == si and j == sj:
        # print("shark")
        return False

    return True


def is_shark_valid(i,j):
    if 0 <= i <= 3 and 0 <= j <= 3:
        return True
    return False

# 훈련시작
def practice(fishbowl, num):
    global si
    global sj

    new_fishbowl = [[[] for _ in range(4)] for _ in range(4)]

    # 물고기들 움직이기
    for i in range(4):
        for j in range(4):
            fishes = fishbowl[i][j]
            for fish in fishes:
                move = False
                for k in range(8):
                    ni = i + fish_dxy[((fish-k-1) % 8) + 1][0]
                    nj = j + fish_dxy[((fish-k-1) % 8) + 1][1]
                    if is_fish_valid(ni, nj):
                        move = True
                        new_fishbowl[ni][nj].append(((fish-k-1) % 8) + 1)
                        break

                if not move:
                    new_fishbowl[i][j].append(fish)

    # 상어 움직이기
    max_cnt = -1
    shark_move = []
    for i in range(4):
        nsi = si + shark_dxy[i][0]
        nsj = sj + shark_dxy[i][1]
        if not is_shark_valid(nsi,nsj):
            continue
        for j in range(4):
            nnsi = nsi + shark_dxy[j][0]
            nnsj = nsj + shark_dxy[j][1]
            if not is_shark_valid(nnsi, nnsj):
                continue
            for k in range(4):
                cnt = 0
                nnnsi = nnsi + shark_dxy[k][0]
                nnnsj = nnsj + shark_dxy[k][1]
                if not is_shark_valid(nnnsi, nnnsj):
                    continue
                visited = set()
                visited.add((nsi,nsj))
                visited.add((nnsi,nnsj))
                visited.add((nnnsi,nnnsj))
                for vi,vj in visited:
                    cnt += len(new_fishbowl[vi][vj])


                if cnt > max_cnt:
                    max_cnt = cnt
                    shark_move = [[nsi,nsj], [nnsi, nnsj], [nnnsi, nnnsj]]

    # 물고기 잡아먹기
    for ni, nj in shark_move:
        if new_fishbowl[ni][nj]:
            blood_smell[ni][nj] = num
            new_fishbowl[ni][nj].clear()



    si = shark_move[-1][0]
    sj = shark_move[-1][1]

    # 냄새빼기
    for i in range(4):
        for j in range(4):
            if blood_smell[i][j] == num - 2:
                blood_smell[i][j] = 0


    # 복제실행
    for i in range(4):
        for j in range(4):
            new_fishbowl[i][j].extend(fishbowl[i][j])


    return new_fishbowl

for n in range(S):
    fishbowl = practice(fishbowl, n+1)


answer = 0
for i in range(4):
    for j in range(4):
        answer += len(fishbowl[i][j])

print(answer)



















