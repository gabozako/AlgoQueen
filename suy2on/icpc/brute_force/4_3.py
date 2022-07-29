N = int(input())
answer = [N] * N
front = list(map(int, input().split()))

for i in range(N-1):
    j = 0
    tall = 0
    while j < N:
        if tall == front[i] and answer[j] == N:
            break
        if answer[j] > i+1:
            tall += 1
        j += 1
    answer[j] = i+1


print(*answer)

