# 회전하기전에 행렬[i][j] = (i-1) x columns + j
def solution(rows, columns, queries):
    answer = []
    board = [ [0] * columns for _ in range(rows)]

    # 유효성검사
    def is_valid(r,c, query):
        r1, c1, r2, c2 = query
        if r1 <= r <= r2 and c1 <= c <= c2:
            return True

        return False

    # 보드초기화
    for row in range(rows):
        for col in range(columns):
            board[row][col] = row * columns + col + 1

    # 쿼리적용
    for query in queries:
        r1, c1, r2, c2 = query

        # 오른쪽
        cur = [r1,c1]
        cur_val = board[r1-1][c1-1]
        result = cur_val
        while True:
            if not is_valid(cur[0], cur[1]+1, query):
                break
            next_val = board[cur[0]-1][cur[1]] # 다음 값 저장
            result = min(result, next_val)
            board[cur[0]-1][cur[1]] = cur_val # 덮어쓰기
            cur[1] += 1 # 오른쪽으로 움직이기
            cur_val = next_val

        # 아래쪽
        while True:
            if not is_valid(cur[0]+1, cur[1], query):
                break
            next_val = board[cur[0]][cur[1]-1] # 다음 값 저장
            result = min(result, next_val)
            board[cur[0]][cur[1]-1] = cur_val # 덮어쓰기
            cur[0] += 1 # 아래쪽으로 움직이기
            cur_val = next_val


        # 왼쪽
        while True:
            if not is_valid(cur[0], cur[1]-1, query):
                break
            next_val = board[cur[0]-1][cur[1]-2] # 다음 값 저장
            result = min(result, next_val)
            board[cur[0]-1][cur[1]-2] = cur_val # 덮어쓰기
            cur[1] -= 1 # 왼쪽으로 움직이기
            cur_val = next_val


        # 위쪽
        while True:
            if not is_valid(cur[0]-1, cur[1], query):
                break
            next_val = board[cur[0]-2][cur[1]-1] # 다음 값 저장
            result = min(result, next_val)
            board[cur[0]-2][cur[1]-1] = cur_val # 덮어쓰기
            cur[0] -= 1 # 위쪽으로 움직이기
            cur_val = next_val

        answer.append(result)



    return answer