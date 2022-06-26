import sys

input = sys.stdin.readline

N = int(input())

answer = []
stack = []
for _ in range(N):
    request = input().split()
    if request[0] == "push":
        stack.append(request[1])
    elif request[0] == "top":
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)

    elif request[0] == "pop":
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)

    elif request[0] == "empty":
        answer.append(int(len(stack) == 0))
    else:
        answer.append(len(stack))

for a in answer:
    print(a)