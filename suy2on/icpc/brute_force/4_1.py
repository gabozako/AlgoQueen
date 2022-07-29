N = int(input())
answer = 0

for num in range(1, N+1):
    if num < 100:
        answer += 1
        continue

    diff = set()
    num = str(num)
    for i in range(len(num)-1):
        diff.add(int(num[i+1]) - int(num[i]))

    if len(diff) == 1:
        answer += 1

print(answer)
