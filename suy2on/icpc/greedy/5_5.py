N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0

for i in range(N):
    answer += numbers[i] * (N-i)

print(answer)
