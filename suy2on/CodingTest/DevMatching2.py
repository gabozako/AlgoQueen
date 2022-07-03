def is_valid(i, j, m):
    if 0 <= i <= m and 0 <= j <= m:
        return True

    else:
        return False


def solution(n, horizontal):
    m = 1
    clean = 1
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = 1
    pos = [0,0]

    while clean < n * n:
        if horizontal:
            pos[1] += 1
            horizontal = not horizontal

            # 아래
            while True:
                clean += 1
                answer[pos[0]][pos[1]] = clean
                if is_valid(pos[0] + 1, pos[1], m):
                    pos[0] += 1
                else:
                    break

            horizontal = not horizontal
            pos[1] -= 1

            # 왼쪽
            while True:
                clean += 1
                answer[pos[0]][pos[1]] = clean
                if is_valid(pos[0], pos[1]-1, m):
                    pos[1] -= 1
                else:
                    break

            horizontal = not horizontal
            m += 1


        else:
            pos[0] += 1
            horizontal = not horizontal
            # 오른쪽
            while True:
                clean += 1
                answer[pos[0]][pos[1]] = clean
                if is_valid(pos[0], pos[1] +1, m):
                    pos[1] += 1
                else:
                    break

            horizontal = not horizontal
            pos[0] -= 1

            # 위
            while True:
                clean += 1
                answer[pos[0]][pos[1]] = clean
                if is_valid(pos[0]-1, pos[1], m):
                    pos[0] -= 1
                else:
                    break

            horizontal = not horizontal
            m += 1

    return answer




print(solution(5, True))

