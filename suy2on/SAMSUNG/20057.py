import sys
import math
input = sys.stdin.readline

# 좌하우상
direction = [[0,-1],[1,0],[0,1],[-1,0]]

N = int(input())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

# 시작
si = N // 2
sj = N // 2

def is_valid(i,j):
    if 0 <= i <= N-1 and 0 <= j <= N-1:
        return True
    return False

def print_board():
    print(answer)
    for i in range(N):
        print(A[i])
    print("==========")

def sand_move(direction):
    r, c = direction
    if r:
        return [
            [0 * r, -1, 1],
            [0 * r, 1, 1],
            [1 * r, -1, 7],
            [1 * r, 1, 7],
            [1 * r, -2, 2],
            [1 * r, 2, 2],
            [2 * r, -1, 10],
            [2 * r, 1, 10],
            [3 * r, 0, 5]
        ]
    else:
        return [
            [-1,0 * c, 1],
            [1,0 * c, 1],
            [-1,1 * c, 7],
            [1,1 * c, 7],
            [-2, 1 * c, 2],
            [2, 1 * c, 2],
            [-1,2 * c, 10],
            [1,2 * c, 10],
            [0,3 * c, 5]
        ]


answer = 0

# 소멸전까지 돌기
for num in range((N-1) * 2):
    d = direction[num % 4]
    distance = num // 2 + 1
    move = sand_move(d)

    for _ in range(distance):
        ni = si + d[0]
        nj = sj + d[1]
        original = A[ni][nj]
        for dr, dc, percent in move:
            m_sand = math.floor(original * percent * 0.01)
            if is_valid(si+dr, sj+dc):
                A[si+dr][sj+dc] += m_sand
            else:
                answer += m_sand
            A[ni][nj] -= m_sand
        if is_valid(ni+d[0], nj+d[1]):
            A[ni+d[0]][nj+d[1]] += A[ni][nj]
        else:
            answer += A[ni][nj]

        A[ni][nj] = 0
        # 한칸이동
        si = ni
        sj = nj

# 마지막 돌기
d = [0,-1]
distance = N - 1
move = sand_move(d)
for _ in range(distance):
    ni = si + d[0]
    nj = sj + d[1]
    original = A[ni][nj]
    for dr, dc, percent in move:
        m_sand = math.floor(original * 0.01 * percent)
        if is_valid(si + dr, sj + dc):
            A[si + dr][sj + dc] += m_sand
        else:
            answer += m_sand
        A[ni][nj] -= m_sand
    if is_valid(ni + d[0], nj + d[1]):
        A[ni + d[0]][nj + d[1]] += A[ni][nj]
    else:
        answer += A[ni][nj]

    A[ni][nj] = 0
    # 한칸이동
    si = ni
    sj = nj




print(answer)








