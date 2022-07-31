def solution(key, lock):
    N = len(lock)
    M = len(key)
    lockBoard = [[0] * (2 * M + N - 2) for _ in range(2 * M + N - 2)]
    for i in range(N):
        for j in range(N):
            lockBoard[M - 1 + i][M - 1 + j] = lock[i][j]
    hole = 0

    # 자물쇠 구멍 세기
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                hole += 1

    # 겹치는 구간인가
    def is_lock(r, c):
        if M - 1 <= r <= M + N - 2 and M - 1 <= c <= M + N + 2:
            return True
        return False

    # 0도 회전 매칭
    def is_matching0(si, sj):
        cnt = 0
        for i in range(M):
            for j in range(M):
                if is_lock(si + i, sj + j):
                    if lockBoard[si + i][sj + j] == key[i][j] and key[i][j] == 1:
                        return False
                    elif lockBoard[si + i][sj + j] == 0 and key[i][j] == 1:
                        cnt += 1

        return cnt == hole

    # 90도 회전 매칭
    def is_matching90(si, sj):
        cnt = 0
        for i in range(M):
            for j in range(M):
                if is_lock(si + i, sj + j):
                    if lockBoard[si + i][sj + j] == key[j][M - 1 - i] and key[j][M - 1 - i] == 1:
                        return False
                    elif lockBoard[si + i][sj + j] == 0 and key[j][M - 1 - i] == 1:
                        cnt += 1

        return cnt == hole

    def is_matching180(si, sj):
        cnt = 0
        for i in range(M):
            for j in range(M):
                if is_lock(si + i, sj + j):
                    if lockBoard[si + i][sj + j] == key[M - 1 - i][M - 1 - j] and key[M - 1 - i][
                        M - 1 - j] == 1:
                        return False
                    elif lockBoard[si + i][sj + j] == 0 and key[M - 1 - i][M - 1 - j] == 1:
                        cnt += 1

        return cnt == hole

    def is_matching270(si, sj):
        cnt = 0
        for i in range(M):
            for j in range(M):
                if is_lock(si + i, sj + j):
                    if lockBoard[si + i][sj + j] == key[M - 1 - j][i] and key[M - 1 - j][i] == 1:
                        return False
                    elif lockBoard[si + i][sj + j] == 0 and key[M - 1 - j][i] == 1:
                        cnt += 1

        return cnt == hole

    for i in range(M + N - 1):
        for j in range(M + N - 1):
            if is_matching0(i, j) or is_matching90(i, j) or is_matching180(i, j) or is_matching270(i, j):
                return True

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))