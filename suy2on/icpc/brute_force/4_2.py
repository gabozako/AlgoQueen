import itertools
import sys

input = sys.stdin.readline
N = int(input())
ss = []
bs = []
answer = float('inf')

for _ in range(N):
    s, b = map(int, input().split())
    ss.append(s)
    bs.append(b)

for mask in itertools.product([0,1], repeat=N):
    ns = 1
    nb = 0
    if sum(mask): # 재료가 있는 경우
        for i in range(N):
            if mask[i]:
                ns *= ss[i]
                nb += bs[i]
        answer = min(answer, abs(ns-nb))

print(answer)
