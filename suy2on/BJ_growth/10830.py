import sys
import collections

input = sys.stdin.readline
N, B = map(int, input().split())
A = []
mod = 1000

# 처음부터 나머지로 넣기
for _ in range(N):
    numbers = list(map(int, input().split()))
    for i in range(N):
        numbers[i] = numbers[i]%mod
    A.append(numbers)

memo = collections.defaultdict(list)

# 행렬곱
def matrix_multiple(mat1, mat2):
    result = []
    for i in range(N):
        sub = []
        for j in range(N):
            res = 0
            for k in range(N):
                res += mat1[i][k] * mat2[k][j]
            sub.append(res%mod)
        result.append(sub)

    return result

# 제곱 분할정복
def power(b):
    if b == 1:
        return A

    mid = b // 2
    if not memo[mid]:
        memo[mid] = power(mid)

    if not memo[b-mid]:
        memo[b-mid] = power(b-mid)
    return matrix_multiple(memo[mid], memo[b-mid])


for p in power(B):
    print(*p)