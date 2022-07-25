import sys

input = sys.stdin.readline

N = int(input())
for i in range(N):
    ps = input().rstrip()
    stack = []

    for char in ps:
        if char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    if stack:
        print("NO")
    else:
        print("YES")
