# 순열
import itertools

N, M = map(int, input().split())

for permu in itertools.permutations(range(1,N+1), M):
    print(*permu)