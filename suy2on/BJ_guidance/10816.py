import collections

N = int(input())
freqs = collections.defaultdict(int)

numbers = input().split()

for number in numbers:
    freqs[number] += 1

M = int(input())
nums = input().split()

for num in nums:
    print(freqs[num], end=" ")


