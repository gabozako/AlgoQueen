### 더러운 방 개수 알아야함
### 최소로 만들 비용 : 이동거리
### 끝내는 조건
### 1) 큐가 비었다 -> 더러운방이 있다면 , 없다면
### 2) 더러운 방이 0이 되었다 -> 바로 비용반환
import sys
import collections

input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dirty_count():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == "*":
                cnt += 1

    return cnt


def is_valid(r, c):
    if 0 <= r <= R - 1 and 0 <= c <= C - 1 and board[r][c] != "x":
        return True
    return False


def find_vaccum():
    for i in range(R):
        for j in range(C):
            if board[i][j] == "o":
                return [i, j]


def clean_up():
    costs = [[[float('inf'), 0] for _ in range(C) ]for _ in range(R) ]
    queue = collections.deque()
    dirty = dirty_count()

    queue.append([find_vaccum(), 0, 0])

    while queue:
        pos, dis, clean = queue.popleft()

        if costs[pos[0]][pos[1]][0] < dis and clean == costs[pos[0]][pos[1]][1]:
            continue
        print(pos, dis, clean)
        costs[pos[0]][pos[1]][0] = dis
        if board[pos[0]][pos[1]] == "*":  # 먼지면
            clean += 1
        if clean == dirty: # 청소끝
            return dis
        costs[pos[0]][pos[1]][0] = clean
        for i in range(4):
            rr = pos[0] + dr[i]
            cc = pos[1] + dc[i]
            if is_valid(rr, cc):
                queue.append([[rr, cc], dis + 1, clean])

    return -1 # 더러운경우


while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break
    board = []
    for _ in range(R):
        board.append(list(input().rstrip()))

    print(clean_up())
