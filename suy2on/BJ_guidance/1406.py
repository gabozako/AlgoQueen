
## 둘을 나눠서 푸는문제 stack 2개로 나누기 (자료구조 2개로 나누기!!!)

import sys

lstack = []
rstack = []
for char in input():
    lstack.append(char)
N = int(input())
input = sys.stdin.readline

for _ in range(N):
    request = input().split()

    if request[0] == "L":
        if lstack:
            rstack.append(lstack.pop())
    elif request[0] == "D":
        if rstack:
            lstack.append(rstack.pop())
    elif request[0] == "B":
        if lstack:
            lstack.pop()
    else:
        lstack.append(request[1])

print("".join(lstack) + "". join(reversed(rstack)))