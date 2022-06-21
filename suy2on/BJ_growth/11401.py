# A = n!
# B = (n-k)!k!
# B^(-1) = B^(P-2) % P
# A % P * (B^(P-2) % P) % P
# 곱셈 덧셈에는 모듈러 해도 상관 없음

import collections

n, k = map(int, input().split())
P = 1000000007

def factorial(num):
    result = 1
    for i in range(1, num+1):
        result = result * i % P

    return result

# 메모이제이션 : 배열로 하기엔 크기가 너무 로커짐 -> 다 쓰는거 아니니까 딕셔너리
powers = collections.defaultdict(int)

# 분할정복 -> 쪼개서 1될 때까지 + 메모이제이션
def power(s,t):
    if t == 1:
        return s

    mid = t // 2
    if not powers[mid]:
        powers[mid] = power(s, mid) % P
    if not powers[t-mid]:
        powers[t-mid] = power(s, t-mid) % P
    return powers[mid] * powers[t-mid] % P


# n!
A = factorial(n)
# k!(n-k)!
B = factorial(n-k) * factorial(k)
# b^(p-2) % p
B = power(B, P-2)

print(A * B % P)


