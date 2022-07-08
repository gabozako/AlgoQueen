def solution(board, skill):
    answer = 0

    # 액션
    for sk in skill:
        action, r1, c1, r2, c2, degree = sk
        if action == 1:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] -= degree
        else:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] += degree

    # 파괴되지 않은 건물
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] > 0:
                answer += 1

    return answer


