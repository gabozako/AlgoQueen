import sys
import collections

input = sys.stdin.readline
answer = 0

N, K = map(int, input().split())
fishbowl = [[-1] * N for _ in range(N)]

fishbowl[-1] = list(map(int, input().split()))

def is_valid(i,j):
    if 0 <= i <= N-1 and 0 <= j <= N-1 and fishbowl[i][j] != -1:
        return True
    return False

def print_board(num):
    print(num)
    for i in range(N):
        print(fishbowl[i])

    print("=================")

def print_small_board():
    for i in range(N):
        print(fishbowl[i])
    print("*****************")



# 물고기 수 가장 적은 어항 모두에 한마리씩 추가
def plus_fish():
    min_fish = float('inf')
    min_fish_list = []
    for i in range(N):
        if fishbowl[-1][i] == -1:
            break
        if min_fish > fishbowl[-1][i]:
            min_fish = fishbowl[-1][i]
            min_fish_list.clear()
            min_fish_list.append(i)
        elif min_fish == fishbowl[-1][i]:
            min_fish_list.append(i)

    for i in min_fish_list:
        fishbowl[-1][i] += 1



# 공중부양 1
def levitation1():
    # 가장 왼쪽 어항을 오른쪽 위에 쌓기
    fishbowl[-2][1] = fishbowl[-1][0]
    fishbowl[-1][0] = -1

    ## 반복 (맨오른쪽 밑이 바닥이 아닐때까지)
    # 2개 이상 쌓인 어항 모두 공중부양
    C = 1
    pre_C = 1
    while True:
        levitation = collections.deque()
        while C < N:
            if fishbowl[N-2][C] == -1:
                break
            for i in range(N-1,-1,-1):
                if fishbowl[i][C] == -1:
                    break
                levitation.append(fishbowl[i][C])
                fishbowl[i][C] = -1
            C += 1

        print(C, levitation)
        print_small_board()

        R = len(levitation) // (C - pre_C)

        # 90회전한 것을 올릴 수 없으면 복구하고 끝
        if R > N-C:
            for j in range(pre_C, C):
                for i in range(N-1, N-1-R, -1):
                    fishbowl[i][j] = levitation.popleft()
            break

        #90도 회전 -> 바닥에 있는 어항에 올려놓기
        for i in range(N-1-(C-pre_C), N-1):
            for j in range(R):
                fishbowl[i][C+j] = levitation.popleft()

        pre_C = C

    return pre_C


## 물고기 수 조절
def control_fish():
    # 인접한 어항에 물고기 수 차이를 5로 나눈 몫 : d
    # d > 0 많은곳에서 적은 곳으로 d마리 보내주기
    cnt_up_down = collections.defaultdict(int)

    for i in range(N):
        for j in range(N):
            if not is_valid(i,j):
                continue
            # 아래
            if is_valid(i+1,j):
                d = abs(fishbowl[i+1][j] - fishbowl[i][j]) // 5
                if d > 0:
                    if fishbowl[i+1][j] > fishbowl[i][j]:
                        cnt_up_down[(i+1,j)] -= d
                        cnt_up_down[(i,j)] += d
                    else:
                        cnt_up_down[(i + 1, j)] += d
                        cnt_up_down[(i, j)] -= d
            # 오른쪽
            if is_valid(i, j+1):
                d = abs(fishbowl[i][j+1] - fishbowl[i][j]) // 5
                if d > 0:
                    if fishbowl[i][j+1] > fishbowl[i][j]:
                        cnt_up_down[(i, j+1)] -= d
                        cnt_up_down[(i, j)] += d
                    else:
                        cnt_up_down[(i, j+1)] += d
                        cnt_up_down[(i, j)] -= d

    for key in cnt_up_down.keys():
        i, j = key
        fishbowl[i][j] += cnt_up_down[key]


## 어항 일렬
# 왼쪽부터 아래부터 위
def serialization(C):
    new_fishbowl = [[-1] * N for _ in range(N)]
    fishs = []
    print(C)
    for j in range(C,N):
        for i in range(N-1, -1, -1):
            if fishbowl[i][j] == -1:
                break
            fishs.append(fishbowl[i][j])

    new_fishbowl[-1] = fishs

    return new_fishbowl


## 두번째 공중부양 2번 반복

def levitation2():
# 왼쪽 N/2만큼 공중부양해서 180도 회전 -> 오른쪽에 올리기
    mid = N // 2
    for i in range(mid, N):
        fishbowl[-2][i] = fishbowl[-1][N-1-i]
        fishbowl[-1][N-1-i] = -1

    mid = (N + mid) // 2
    for i in range(mid, N):
        fishbowl[-3][i] = fishbowl[-2][N-1-i]
        fishbowl[-4][i] = fishbowl[-1][N-1-i]
        fishbowl[-2][N - 1 - i] = -1
        fishbowl[-1][N - 1 - i] = -1

    return mid

while True:
    print_board(answer)
    plus_fish()
    print_board(answer)
    c = levitation1()
    print_board(answer)
    control_fish()
    print_board(answer)
    fishbowl = serialization(c)
    print_board(answer)
    c = levitation2()
    print_board(answer)
    control_fish()
    print_board(answer)
    fishbowl = serialization(c)

    print_board(answer)

    min_fish = float('inf')
    max_fish = 0
    for i in range(N):
        min_fish = min(min_fish, fishbowl[-1][i])
        max_fish = max(max_fish, fishbowl[-1][i])

    answer += 1
    if max_fish - min_fish <= K:
        break

print(answer)



