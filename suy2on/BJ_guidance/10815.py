#### 시간복잡도를 따져서 nlogn으로 풀자

### 1. in연산 -> set때문에 가능한건지..ㅎㅎ
import sys

input = sys.stdin.readline

input()
numbers = set(input().split())
input()
nums = input().split()

exist = ""
for num in nums:
    if num in numbers:
        exist += "1 "
    else:
        exist += "0 "

print(exist)

### 2. 딕셔너리 -> 무난 