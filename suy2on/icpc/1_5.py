import sys


def is_valid(x, color):
    if 0 <= x <= N-1 and color == pos[x][1]: # 색깔이 같고 좌표가 범위안에 있어야 함 
        return True
    else:
        return False

input = sys.stdin.readline

N = int(input())
pos = []

for _ in range(N):
    pos.append(list(map(int, input().split())))

pos = sorted(pos, key = lambda x : (x[1],x[0])) # 색깔로 정렬하고 순서대로 좌표순서대로 정렬

answer = 0
for i in range(N):
    result = []
    if is_valid(i-1, pos[i][1]): # 왼쪽
        result.append(pos[i][0] - pos[i-1][0])
    if is_valid(i+1, pos[i][1]): # 오른쪽
        result.append(pos[i+1][0] - pos[i][0])

    if result: # 결과있을 때만 더하기
        answer += min(result)

print(answer)