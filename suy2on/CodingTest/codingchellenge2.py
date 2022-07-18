# 회전하기전에 행렬[i][j] = (i-1) x columns + 1
def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    # 쿼리적용
    for r1, c1, r2, c2 in queries:
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
        cur = board[r1][c1]
        min_num = cur

        # 순서대로 넣기 : 3개씩
        for c in range(c1 + 1, c2 + 1):
            board[r1][c], cur = cur, board[r1][c]
            min_num = min(cur, min_num)
        for r in range(r1 + 1, r2 + 1):
            board[r][c2], cur = cur, board[r][c2]
            min_num = min(cur, min_num)
        for c in range(c2 - 1, c1 - 1, -1):
            board[r2][c], cur = cur, board[r2][c]
            min_num = min(cur, min_num)
        for r in range(r2 - 1, r1 - 1, -1):
            board[r][c1], cur = cur, board[r][c1]
            min_num = min(cur, min_num)

        answer.append(min_num)

    return answer


##### 풀이 2 ######


# 회전하기전에 행렬[i][j] = (i-1) x columns + j
import collections


def solution(rows, columns, queries):
    answer = []
    board = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    # 쿼리적용
    for query in queries:
        r1, c1, r2, c2 = query
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

        result = collections.deque()

        # 순서대로 넣기
        for c in range(c1, c2):
            result.append(board[r1][c])
        for r in range(r1, r2):
            result.append(board[r][c2])
        for c in range(c2, c1, -1):
            result.append(board[r2][c])
        for r in range(r2, r1, -1):
            result.append(board[r][c1])

        answer.append(min(result))
        result.rotate(1)

        # 시계방향으로 회전해서 넣기
        for c in range(c1, c2):
            board[r1][c] = result.popleft()
        for r in range(r1, r2):
            board[r][c2] = result.popleft()
        for c in range(c2, c1, -1):
            board[r2][c] = result.popleft()
        for r in range(r2, r1, -1):
            board[r][c1] = result.popleft()

    return answer