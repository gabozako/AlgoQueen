import sys

input = sys.stdin.readline

N = int(input())

def merge(head, tail):
    if memo[head][tail] != -1:
        return memo[head][tail]

    res = float('inf')
    for p in range(head, tail):
        res = min(res, merge(head,p) + merge(p+1, tail))


    memo[head][tail] = res + subsum[tail+1] - subsum[head]

    return memo[head][tail]


for i in range(N):
    M = int(input())
    pages = list(map(int, input().rstrip().split()))
    subsum = [0]
    # 부분합
    for i in range(M):
        subsum.append(pages[i] + subsum[i])

    memo = [[-1] * M for _ in range(M)]
    # 초기화
    for j in range(M):
        for k in range(M):
            if j == k:
                memo[j][k] = 0
            elif j + 1 == k:
                memo[j][k] = pages[j] + pages[k]

    print(merge(0, M-1))
