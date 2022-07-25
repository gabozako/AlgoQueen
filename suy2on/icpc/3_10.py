import sys

input = sys.stdin.readline
N = int(input())
MOD = 10**9 + 7

numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

for number in numbers:
    number[0] *= number[1]
    number[1] -= 1

answer = 0
for number in numbers:
    answer += number[0] * pow(2,number[1],MOD)

print(answer % MOD)