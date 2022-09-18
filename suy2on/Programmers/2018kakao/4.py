def solution(m, n, board):
    answer = 0
    board_arr = []

    for b in board:
        board_arr.append(list(b))

    while True:
        # 블록탐색
        remove = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board_arr[i][j] and board_arr[i][j] == board_arr[i + 1][j] == board_arr[i][j + 1] == board_arr[i + 1][j + 1]:
                    remove.append([i, j])

        # 더 이상 지울거 없음
        if not remove:
            return answer

        # 지우기
        for rm in remove:
            i, j = rm
            if board_arr[i][j]:
                board_arr[i][j] = ""
                answer += 1
            if board_arr[i + 1][j]:
                board_arr[i + 1][j] = ""
                answer += 1
            if board_arr[i][j + 1]:
                board_arr[i][j + 1] = ""
                answer += 1
            if board_arr[i + 1][j + 1]:
                board_arr[i + 1][j + 1] = ""
                answer += 1

        # 공백 채우기
        for i in range(m-2,-1,-1):
            for j in range(n):
                if board_arr[i][j]:
                    p = i + 1
                    while p < m and not board_arr[p][j]:
                        board_arr[p][j], board_arr[p - 1][j] = board_arr[p - 1][j], board_arr[p][j]
                        p += 1

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))