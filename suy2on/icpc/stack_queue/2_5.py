import sys

input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    action = input().rstrip().split()

    if action[0] == "size":
        print(len(queue))
    elif action[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif action[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif action[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif action[0] == "pop":
        if queue:
            print(queue[0])
            queue = queue[1:]
        else:
            print(-1)
    else:
        queue.append(int(action[1]))



