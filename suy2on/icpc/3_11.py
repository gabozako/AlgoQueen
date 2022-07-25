## 두 배열의 합
import sys
import collections

input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
aSub = collections.defaultdict(int)
bSub = collections.defaultdict(int)
answer = 0

for i in range(N):
    total = 0
    for j in range(i,N):
        total += A[j]
        aSub[total] += 1

for i in range(M):
    total = 0
    for j in range(i,M):
        total += B[j]
        bSub[total] += 1

for key in aSub.keys():
    answer += aSub[key] * bSub[T-key]

print(answer)

