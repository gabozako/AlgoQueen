def solution(board, skill):
    R = len(board)
    C = len(board[0])
    answer = 0

    result = [[0] * (C + 1) for _ in range(R + 1)]

    # 표시
    for sk in skill:
        t, r1, c1, r2, c2, degree = sk

        if t == 1:  # 적
            result[r1][c1] -= degree
            result[r2 + 1][c2 + 1] -= degree
            result[r1][c2 + 1] += degree
            result[r2 + 1][c1] += degree
        else:
            result[r1][c1] += degree
            result[r2 + 1][c2 + 1] += degree
            result[r1][c2 + 1] -= degree
            result[r2 + 1][c1] -= degree

    # 계산
    for i in range(R):
        for j in range(1, C):
            result[i][j] += result[i][j - 1]

    for j in range(C):
        for i in range(1, R):
            result[i][j] += result[i - 1][j]

    for i in range(R):
        for j in range(C):
            if result[i][j] + board[i][j] > 0:
                answer += 1

    return answer