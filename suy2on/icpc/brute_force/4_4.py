## N-queen
N = int(input())
answer = 0
col = [0] * 15

def is_valid(row):
    for i in range(row):
        if col[i] == col[row] or abs(row-i) == abs(col[row] - col[i]):
            return False

    return True

def nqueen(row):
    global answer

    if row == N:
        answer += 1
        return

    for i in range(N):
        col[row] = i
        if is_valid(row):
            nqueen(row+1)
        col[row] = 0


nqueen(0)
print(answer)