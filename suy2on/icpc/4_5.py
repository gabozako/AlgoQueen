## 스도쿠
sudocu = []
for _ in range(9):
    sudocu.append(list(map(int, input().split())))

holes = []
for i in range(9):
    for j in range(9):
        if not sudocu[i][j]:
            holes.append([i,j])

def is_valid(n):
    row = holes[n][0]
    col = holes[n][1]

    # 가로 세로 확인
    for i in range(9):
        if i != row and sudocu[i][col] == sudocu[row][col]:
            return False
        if i != col and sudocu[row][i] == sudocu[row][col]:
            return False

    # 네모박스 확인
    rs = (row // 3) * 3
    cs = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if row != rs+i and col != cs+j and sudocu[rs+i][cs+j] == sudocu[row][col]:
                return False


    return True

finish = False

def dfs(n):
    global finish

    if finish:
        return

    if n == len(holes):
        for i in range(9):
            print(*sudocu[i])
        finish = True
        return

    for i in range(1,10):
        sudocu[holes[n][0]][holes[n][1]] = i
        if is_valid(n):
            dfs(n+1)
        sudocu[holes[n][0]][holes[n][1]] = 0

dfs(0)



