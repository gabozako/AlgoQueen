#### 1 이진탐색 : O(NlogN)
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

M = int(input())
nums = list(map(int, input().split()))

def bisearch(head, tail, num):
    if head > tail:
        return 0

    mid = head + (tail - head) // 2
    if num == numbers[mid]:
        return 1
    elif num > numbers[mid]:
        return bisearch(mid+1, tail, num)
    else:
        return bisearch(head, mid-1, num)

exist = []
for num in nums:
    exist.append(bisearch(0, N-1, num))

for e in exist:
    print(e)


#### 2. 딕셔너리 : O(N)

# 시간제한이 1초인 문제를 만났을 때 일반적인 기준은 다음과 같습니다
# N의 범위가 500인 경우: 시간 복잡도가 O(N³)인 알고리즘을 설계하면 문제를 풀 수 있음
# N의 범위가 2,000인 경우: 시간 복잡도가 O(N²)인 알고리즘을 설계하면 문제를 풀 수 있음
# N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있음
# N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있음