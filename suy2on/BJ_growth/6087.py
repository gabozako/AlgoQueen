import sys
import collections

input = sys.stdin.readline

C, R = map(int, input().split())
board = []
costs = [[float('inf')] * C for _ in range(R)]
queue = collections.deque()
razers = []

for _ in range(R):
    board.append(list(input().rstrip()))


# 유효성검사
def is_valid(i, j):
    if 0 <= i <= R - 1 and 0 <= j <= C - 1 and board[i][j] != '*':
        return True
    else:
        return False

# 레이저 찾기
def find_razer():
    for i in range(R):
        for j in range(C):
            if board[i][j] == "C":
                razers.append([i, j])

            if len(razers) == 2:
                return


# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 레이저 1에서 전체 출발
def bfs():
    for i in range(4):
        rr = razers[0][0] + dr[i]
        cc = razers[0][1] + dc[i]
        if is_valid(rr, cc):
            queue.append([[rr,cc], i, 0])

    while queue:
        node, direction, cost = queue.popleft()

        if node == razers[1]:
            costs[node[0]][node[1]] = min(costs[node[0]][node[1]], cost)
            continue
        if costs[node[0]][node[1]] >= cost:
            costs[node[0]][node[1]] = cost # 최소갱신
            for i in range(4):
                rr = node[0] + dr[i]
                cc = node[1] + dc[i]
                if is_valid(rr, cc):
                    if direction != i:
                        queue.append([[rr, cc], i, cost+1])
                    else:
                        queue.append([[rr, cc], i, cost])

find_razer()
bfs()
print(costs[razers[1][0]][razers[1][1]])

