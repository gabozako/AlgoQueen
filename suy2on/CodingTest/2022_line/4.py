from typing import List
import collections


def solution(wall: List[str]) -> List[List[int]]:
    R = len(wall)
    C = len(wall[0])
    drc = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # 유효성체크
    def is_valid(i, j):
        if 0 <= i <= R - 1 and 0 <= j <= C - 1:
            return True
        return False

    answer = [[0] * C for _ in range(R)]

    queue = collections.deque()
    queue.append([R - 1, 0, 1])
    answer[R - 1][0] = 1

    while queue:
        r, c, holder = queue.popleft()

        # 상하좌우
        for i in range(4):
            nr = r + drc[i][0]
            nc = c + drc[i][1]
            if is_valid(nr, nc) and wall[nr][nc] == "H":
                if not answer[nr][nc]:
                    answer[nr][nc] = holder + 1
                    queue.append([nr, nc, holder + 1])

        # 바로 2칸 위
        if is_valid(r - 2, c) and wall[r - 2][c] == "H":
            if wall[r - 1][c] == ".":
                if not answer[r - 2][c]:
                    answer[r - 2][c] = holder + 1
                    queue.append([r - 2, c, holder + 1])

        # 오른쪽 대각선 위
        if is_valid(r - 1, c + 1) and wall[r - 1][c + 1] == "H":
            if wall[r - 1][c] == "." and wall[r][c + 1] == ".":
                if not answer[r - 1][c + 1]:
                    answer[r - 1][c + 1] = holder + 1
                    queue.append([r - 1, c + 1, holder + 1])

        # 왼쪽 대각선 위
        if is_valid(r - 1, c - 1) and wall[r - 1][c - 1] == "H":
            if wall[r - 1][c] == wall[r][c - 1] == ".":
                if not answer[r - 1][c - 1]:
                    answer[r - 1][c - 1] = holder + 1
                    queue.append([r - 1, c - 1, holder + 1])

        # 왼쪽 2칸
        if is_valid(r, c - 2) and is_valid(r - 1, c - 2) and wall[r][c - 2] == "H":
            if wall[r][c - 1] == wall[r - 1][c] == wall[r - 1][c - 1] == wall[r - 1][c - 2] == ".":
                if not answer[r][c - 2]:
                    answer[r][c - 2] = holder + 1
                    queue.append([r, c - 2, holder + 1])

        # 왼쪽 3칸
        if is_valid(r, c - 3) and is_valid(r - 1, c - 3) and wall[r][c - 3] == "H":
            if wall[r][c - 1] == wall[r][c - 2] == wall[r - 1][c] == wall[r - 1][c - 1] == wall[r - 1][c - 2] == \
                    wall[r - 1][c - 3] == ".":
                if not answer[r][c - 3]:
                    answer[r][c - 3] = holder + 1
                    queue.append([r, c - 3, holder + 1])

        # 오른쪽 2칸
        if is_valid(r, c + 2) and is_valid(r - 1, c + 2) and wall[r][c + 2] == "H":
            if wall[r][c + 1] == wall[r - 1][c] == wall[r - 1][c + 1] == wall[r - 1][c + 2] == ".":
                if not answer[r][c + 2]:
                    answer[r][c + 2] = holder + 1
                    queue.append([r, c + 2, holder + 1])

        # 오른쪽 3칸
        if is_valid(r, c + 3) and is_valid(r - 1, c + 3) and wall[r][c + 3] == "H":
            if wall[r][c + 1] == wall[r][c + 2] == wall[r - 1][c] == wall[r - 1][c + 1] == wall[r - 1][c + 2] == \
                    wall[r - 1][c + 3] == ".":
                if not answer[r][c + 3]:
                    answer[r][c + 3] = holder + 1
                    queue.append([r, c + 3, holder + 1])

    # 도달하지 못하는 홀더
    for i in range(R):
        for j in range(C):
            if wall[i][j] == "H" and not answer[i][j]:
                answer[i][j] = -1

    return answer