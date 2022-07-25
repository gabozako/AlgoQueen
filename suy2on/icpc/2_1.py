import collections

queue = collections.deque()
N,K = map(int, input().split())
result = []
for i in range(N):
    queue.append(i+1)

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())

    result.append(str(queue.popleft()))

print("<" + ", ".join(result) +">")


