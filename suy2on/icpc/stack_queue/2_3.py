import collections

N, K, M = map(int, input().split())

deq = collections.deque()
result = []
for i in range(N):
    deq.append(i+1)

right = True
count = 0

while deq:
    if right:
        for _ in range(K-1):
            deq.append(deq.popleft())

        result.append(str(deq.popleft()))
        count += 1
        if count % M == 0:
            right = False
    else:
        for _ in range(K - 1):
            deq.appendleft(deq.pop())

        result.append(str(deq.pop()))
        count += 1
        if count % M == 0:
            right = True


print("\n".join(result))
