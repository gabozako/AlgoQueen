# 마법사 상어와 블리자드
import sys
input = sys.stdin.readline

# 좌하우상
drc = [[0,-1],[1,0],[0,1],[-1,0]]
shark_drc = [[-1,0],[1,0],[0,-1],[0,1]]
N, M = map(int, input().split())
board = []

si = N // 2
sj = N // 2

for _ in range(N):
    board.append(list(map(int, input().split())))

def is_valid(i,j):
    if 0<= i <= N-1 and 0<= j <= N-1:
        return True
    return False

def make_board(serial):
    new_board = [[0] * N for _ in range(N)]
    serial.reverse()
    ni = si
    nj = sj
    for i in range(2*(N-1)):
        loops = i//2 + 1
        dir = drc[i%4]
        for _ in range(loops):
            ni += dir[0]
            nj += dir[1]
            new_board[ni][nj] = serial.pop()

    for _ in range(N-1):
        nj += - 1
        new_board[ni][nj] = serial.pop()

    return new_board

def make_serial(bd):
    new_serial = []
    ni = si
    nj = sj
    for i in range(2*(N-1)):
        loops = i // 2 + 1
        dir = drc[i % 4]
        for _ in range(loops):
            ni += dir[0]
            nj += dir[1]
            new_serial.append(bd[ni][nj])

    for _ in range(N-1):
        nj += - 1
        new_serial.append(bd[ni][nj])



    return new_serial



def booming(serial):
    boom = [0] * 3
    # 폭발
    head = 0
    tail = 1
    while tail < len(serial):
        if serial[tail] != serial[head]:
            if tail - head >= 4:
                boom[serial[head]-1] += (tail - head)
                serial[head:tail] = [0] * (tail - head)
            head = tail
        tail += 1

    if tail - head >= 4:
        boom[serial[head] - 1] += (tail - head)
        serial[head:tail] = [0] * (tail - head)

    return 1 * boom[0] + 2 * boom[1] + 3 * boom[2]


answer = 0

def practice(dr,ds):
    global answer

    # 구슬 깨기
    ni = si
    nj = sj
    for _ in range(ds):
        ni += shark_drc[dr-1][0]
        nj += shark_drc[dr-1][1]
        if not is_valid(ni,nj):
            break
        board[ni][nj] = 0

    # 직렬화 및 구슬이동
    serial = make_serial(board)
    while 0 in serial:
        serial.remove(0)


    # 폭발
    while True:
        score = booming(serial)
        if not score:
            break
        answer += score
        # 구슬 이동
        while 0 in serial:
            serial.remove(0)


    ## TODO : serial의 길이가 0이면 ?
    new_serial = []
    # 그룹별 구분 및 새롭게 넣기
    head = 0
    tail = 1
    while tail < len(serial):
        if serial[tail] != serial[head]:
            new_serial.append(tail - head)
            new_serial.append(serial[head])
            head = tail
        tail += 1

    if serial:
        new_serial.append(tail - head)
        new_serial.append(serial[head])


    # 길이 맞춰주기
    if len(new_serial) > (N ** 2) - 1:
        new_serial = new_serial[:(N**2)-1]

    elif len(new_serial) < (N**2) - 1:
        new_serial.extend([0] * ((N**2-1) - len(new_serial)))

    # 다시 보드로 만들기
    return make_board(new_serial)


for _ in range(M):
    dr, ds = map(int, input().split())
    board = practice(dr,ds)
    # for i in range(N):
    #     print(board[i])
    # print("=======")


print(answer)
























