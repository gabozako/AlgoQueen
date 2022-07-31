## 규칙
# 보(1) : 양끝에 보, 양끝 중에 하나 밑에 기둥
# 기둥(0) : 바닥위, 양끝 중 하나 위에 밑에 보, 밑에 기둥
## 규칙 지키면서 지우거나(0) 추가(1) => 결과 반환 (규칙위반 무시)
def solution(n, build_frame):
    board = [[[0] * 2 for _ in range(n + 1)] for _ in range(n + 1)]

    def is_valid(i, j):
        if 0 <= i <= n and 0 <= j <= n:
            return 1

        return 0

    def can_install_pillar(x, y):
        if y == 0:  # 바닥
            return 1
        if board[x][y][1]:
            return 1
        if is_valid(x - 1, y) and board[x - 1][y][1]:
            return 1
        if is_valid(x, y - 1) and board[x][y - 1][0]:
            return 1

        return False

    def can_install_bo(x, y):
        if is_valid(x, y - 1) and board[x][y - 1][0]:
            return 1
        if is_valid(x + 1, y - 1) and board[x + 1][y - 1][0]:
            return 1
        if is_valid(x + 1, y) and is_valid(x - 1, y) and board[x + 1][y][1] and board[x - 1][y][1]:
            return 1

        return False

    for action in build_frame:
        x, y, a, b = action

        if b == 1:  # 설치
            if a == 0:  # 기둥
                if can_install_pillar(x, y):
                    board[x][y][0] = 1

            else:  # 보
                if can_install_bo(x, y):
                    board[x][y][1] = 1

        else:  # 삭제
            if a == 0:  # 기둥
                board[x][y][0] = 0

                if is_valid(x, y + 1) and board[x][y + 1][0]:
                    if not can_install_pillar(x, y + 1):
                        board[x][y][0] = 1

                if is_valid(x, y + 1) and board[x][y + 1][1]:
                    if not can_install_bo(x, y + 1):
                        board[x][y][0] = 1

                if is_valid(x - 1, y + 1) and board[x - 1][y + 1][1]:
                    if not can_install_bo(x - 1, y + 1):
                        board[x][y][0] = 1

            else:  # 보
                board[x][y][1] = 0

                if is_valid(x - 1, y) and board[x - 1][y][1]:
                    if not can_install_bo(x - 1, y):
                        board[x][y][1] = 1

                if is_valid(x + 1, y) and board[x + 1][y][1]:
                    if not can_install_bo(x + 1, y):
                        board[x][y][1] = 1

                if board[x][y][0]:
                    if not can_install_pillar(x, y):
                        board[x][y][1] = 1

                if is_valid(x + 1, y) and board[x + 1][y][0]:
                    if not can_install_pillar(x + 1, y):
                        board[x][y][1] = 1

    # 전체탐색
    result = []
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(2):
                if board[i][j][k]:
                    result.append([i, j, k])

    return sorted(result)