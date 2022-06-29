import sys

input = sys.stdin.readline


N = int(input())
matrixes = []
memo = [[-1] * N for _ in range(N)]

for _ in range(N):
    matrixes.append(list(map(int,input().rstrip().split())))

# 초기화
def init():
    for i in range(N):
        for j in range(N):
            if i == j:
                memo[i][j] = 0
            if j == i+1:
                memo[i][j] = matrixes[i][0] * matrixes[i][1] * matrixes[j][1]


def multiple_matrix(head,tail):
    print(head,tail)
    if memo[head][tail] != -1:
        return memo[head][tail]

    result = float('inf')
    for mid in range(head,tail):
        result = min(result, multiple_matrix(head,mid) + multiple_matrix(mid+1,tail) + matrixes[head][0] * matrixes[mid][1] * matrixes[tail][1])

    memo[head][tail] = result
    return result


init()
multiple_matrix(0,N-1)
print(memo[0][N-1])



