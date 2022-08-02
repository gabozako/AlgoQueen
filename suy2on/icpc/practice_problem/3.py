## 주유소
N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

i = 1
price = prices[0]
total = 0
head = 0
while i < N:
    if prices[i] < price:
        total += price * sum(distances[head:i])
        price = prices[i]
        head = i

    i += 1

total += price * sum(distances[head:])

print(total)

