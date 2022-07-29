## 종이의 개수
import sys

input = sys.stdin.readline
answer = [0,0,0]

N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))



def check(start, n):
    x, y = start
    val = board[x][y]
    for i in range(n):
        for j in range(n):
            if board[x+i][y+j] != val:
                return False

    return True

def paper(start, n):
    x, y = start
    if check(start, n):
        answer[board[x][y]+1] += 1
        return

    gap = n // 3
    for i in range(3):
        for j in range(3):
            paper([x+gap*i, y+gap*j], gap)

paper([0,0], N)

for p in answer:
    print(p)





