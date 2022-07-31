import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

answer = 0
for i in range(N):
    d, K = divmod(K, coins[N-1-i])
    answer += d
    if not K:
        break

print(answer)

