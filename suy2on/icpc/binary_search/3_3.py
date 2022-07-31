## 투포인터응용
N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
answer = float('inf')
answerPair = []

for p1 in range(N-2):
    p2, p3 = p1+1, N-1
    while p2 < p3:
        if solutions[p1] + solutions[p2] + solutions[p3] == 0:
            answer = 0
            answerPair = [p1, p2, p3]
            break

        elif solutions[p1] + solutions[p2] + solutions[p3] < 0:
            if answer > abs(solutions[p1] + solutions[p2] + solutions[p3]):
                answer = abs(solutions[p1] + solutions[p2] + solutions[p3])
                answerPair = [p1, p2, p3]
            p2 += 1

        else:
            if answer > abs(solutions[p1] + solutions[p2] + solutions[p3]):
                answer = abs(solutions[p1] + solutions[p2] + solutions[p3])
                answerPair = [p1, p2, p3]
            p3 -= 1

print(solutions[answerPair[0]], solutions[answerPair[1]], solutions[answerPair[2]])

