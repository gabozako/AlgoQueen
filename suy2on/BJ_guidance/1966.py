import sys
import collections

input = sys.stdin.readline

N = int(input())

for i in range(N):
    M, target = map(int, input().split())
    numbers = list(map(int, input().split()))
    waitQ = collections.deque()
    printStack = []
    middleStack = []

    for j in range(M):
        waitQ.append([numbers[j], j])

    while waitQ:
        while printStack and waitQ[0][0] > printStack[-1][0]:
            middleStack.append(printStack.pop())

        printStack.append(waitQ.popleft())

        while middleStack:
            waitQ.append(middleStack.pop())

    for i in range(M):
        if printStack[i][1] == target:
            print(i+1)
