### 더러운 방 개수 알아야함
### 최소로 만들 비용 : 이동거리
### 끝내는 조건
### 1) 큐가 비었다 -> -1
### 2) 더러운 방이 0이 되었다 -> 바로 비용반환
import sys
import collections

input = sys.stdin.readline
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dirty_record():
    for i in range(R):
        for j in range(C):
            if board[i][j] == "*":
                dirty.append([i,j])


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
    dirty_record()
    queue = collections.deque()
    queue.append([find_vaccum(), 0, 0])

    while queue:
        pos, dis, clean = queue.popleft()

        if visited[pos[0]][pos[1]][clean]: # 같은 먼지를 치우고 방문한 이력있다면
            continue
        print("hear")
        if board[pos[0]][pos[1]] == "*":  # 먼지면
            clean = clean | 1 << dirty.index(pos)
            print(bin(clean))
        if clean == (1 << len(dirty))-1:  # 청소끝
            return dis

        visited[pos[0]][pos[1]][clean] = 1 # 방문
        for i in range(4):
            rr = pos[0] + dr[i]
            cc = pos[1] + dc[i]
            if is_valid(rr, cc):
                queue.append([[rr, cc], dis + 1, clean])

    return -1  # 더러운경우


while True:
    C, R = map(int, input().split())
    if C == 0 and R == 0:
        break
    board = []
    dirty = []
    visited = [[[0] * (1 << 9) for _ in range(C)] for _ in range(R)]
    for _ in range(R):
        board.append(list(input().rstrip()))

    print(clean_up())

