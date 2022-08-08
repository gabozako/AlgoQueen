## 카드높기 : 덱
import collections

N = int(input())
orders = list(map(int, input().split()))
orders.reverse()

answer = collections.deque()

for i in range(N):
    if orders[i] == 1:
        answer.appendleft(i+1)
    elif orders[i] == 2:
        tmp = answer.popleft()
        answer.appendleft(i+1)
        answer.appendleft(tmp)
    else:
        answer.append(i+1)

print(*answer)
