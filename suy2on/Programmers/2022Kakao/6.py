def solution(board, skill):
    answer = 0
    R = len(board)
    C = len(board[0])
    totalSum = [[0] * C for _ in range(R)]

    def is_valid(r, c):
        if 0 <= r <= R - 1 and 0 <= c <= C - 1:
            return True
        return False

    # 누적합 표시 O(M)
    for s in skill:
        action, r1, c1, r2, c2, degree = s
        if action == 1:
            totalSum[r1][c1] -= degree
            if is_valid(r2 + 1, c1):
                totalSum[r2 + 1][c1] += degree
            if is_valid(r1, c2 + 1):
                totalSum[r1][c2 + 1] += degree
            if is_valid(r2 + 1, c2 + 1):
                totalSum[r2 + 1][c2 + 1] -= degree
        else:
            totalSum[r1][c1] += degree
            if is_valid(r2 + 1, c1):
                totalSum[r2 + 1][c1] -= degree
            if is_valid(r1, c2 + 1):
                totalSum[r1][c2 + 1] -= degree
            if is_valid(r2 + 1, c2 + 1):
                totalSum[r2 + 1][c2 + 1] += degree

    # 가로방향 누적합계산 O(N)
    for r in range(R):
        for c in range(1, C):
            totalSum[r][c] += totalSum[r][c - 1]

    # 세로방향 누적합계산 O(N)
    for c in range(C):
        for r in range(1, R):
            totalSum[r][c] += totalSum[r - 1][c]

    # 전체 건물파괴 계산 O(N)
    for r in range(R):
        for c in range(C):
            if board[r][c] + totalSum[r][c] > 0:
                answer += 1

    return answer
