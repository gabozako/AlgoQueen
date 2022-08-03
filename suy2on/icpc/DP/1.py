## 가장 긴 증가하는 부분 수열
# dp[i] : i를 포함한 0-i까지 중 최대 -> 마지막 값을 알아야 증가하는지 아니까
# dp[i] = dp[0] - dp[i-1]까지 중에 서 마지막이 num[i]보다 작은 애들중에 가장큰애  + 1 즉 없을 수도 있다
N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N

for i in range(1,N):
    j = 0
    while j < i:
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
        j += 1


print(max(dp))


