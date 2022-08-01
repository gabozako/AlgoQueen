## k번째 수 : lower bound
N = int(input())
K = int(input())
left = 1
right = N**2

while left < right:
    mid = (left + right) // 2
    total = 0
    for i in range(1, N+1):
        total += min(mid // i, N)

    if total >= K:
        right = mid
    else:
        left = mid + 1

print(left)


