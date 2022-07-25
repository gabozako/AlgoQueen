# 제곱
import collections

A, B, C = map(int, input().split())
dp = collections.defaultdict(int)
dp[0] = 1


def pow(k):
    if dp[k]:
        return dp[k]

    half = k // 2

    if k % 2 == 0:  # 짝수
        dp[k] = (pow(half)* pow(half)) % C
    else:
        dp[k] = (pow(half) * pow(half) * A) % C

    return dp[k]


print(pow(B))
