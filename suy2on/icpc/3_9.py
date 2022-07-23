## 랜선만들기
import sys

input = sys.stdin.readline
K, N = map(int, input().split())
lines = []

for _ in range(K):
    lines.append(int(input()))

left = 1
right = max(lines)

# 랜선길이의 최대를 이분탐색으로 찾기
while left <= right:
    mid = (left + right) // 2

    total = 0
    for line in lines:
        total += line // mid

    if total >= N: # 총 랜선수가 N이상
        left = mid + 1
    else: # 랜선수가 N미만
        right = mid - 1


print(right)
