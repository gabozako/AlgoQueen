## 투포인터
N = int(input())
solutions = list(map(int, input().split()))
head = 0
tail = N-1
answer = float('inf')
answerPair = []

while head < tail:
    if solutions[head] + solutions[tail] == 0:
        answer = 0
        answerPair = [solutions[head], solutions[tail]]
        break

    elif solutions[head] + solutions[tail] < 0:
        if answer > abs(solutions[head] + solutions[tail]):
            answer = abs(solutions[head] + solutions[tail])
            answerPair = [solutions[head], solutions[tail]]
        head += 1

    else:
        if answer > abs(solutions[head] + solutions[tail]):
            answer = abs(solutions[head] + solutions[tail])
            answerPair = [solutions[head], solutions[tail]]
        tail -= 1

print(*answerPair)

