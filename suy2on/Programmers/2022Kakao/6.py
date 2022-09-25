def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])

    total_board = [[0] * (M + 1) for _ in range(N + 1)]

    # 누적합 기록
    for ty, r1, c1, r2, c2, degree in skill:
        if ty == 1:
            total_board[r1][c1] -= degree
            total_board[r1][c2 + 1] += degree
            total_board[r2 + 1][c1] += degree
            total_board[r2 + 1][c2 + 1] -= degree
        else:
            total_board[r1][c1] += degree
            total_board[r1][c2 + 1] -= degree
            total_board[r2 + 1][c1] -= degree
            total_board[r2 + 1][c2 + 1] += degree

    # 누적합 계산
    for i in range(N):
        for j in range(1, M):
            total_board[i][j] += total_board[i][j - 1]

    for j in range(M):
        for i in range(1, N):
            total_board[i][j] += total_board[i - 1][j]

    # 비교
    for i in range(N):
        for j in range(M):
            if board[i][j] + total_board[i][j] > 0:
                answer += 1

    return answer
