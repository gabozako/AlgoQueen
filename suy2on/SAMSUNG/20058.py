import sys
import collections
input = sys.stdin.readline

N, Q = map(int, input().split())
ice = []
drc = [[0,1],[0,-1],[1,0],[-1,0]]

for _ in range(2**N):
    ice.append(list(map(int, input().split())))

LS = list(map(int, input().split()))

def is_valid(i,j):
    if 0 <= i <= 2**N - 1 and 0 <= j <= 2**N - 1:
        return True

    return False

def print_board():
    for i in range(2**N):
        print(ice[i])
    print("===========")


# 90도 회전
def spin_90(L):
    new_ice = [[0] * 2**N for _ in range(2**N)]
    for si in range(0,2**N,2**L):
        for sj in range(0, 2**N, 2**L):
            for i in range(2**L):
                for j in range(2**L):
                    new_ice[si+i][sj+j] = ice[si+2**L-1-j][sj+i]

    return new_ice


def melting():
    new_ice = [[0] * 2**N for _ in range(2**N)]
    for i in range(2 ** N):
        for j in range(2 ** N):
            cnt = 0
            for k in range(4):
                ni = i + drc[k][0]
                nj = j + drc[k][1]
                if is_valid(ni, nj) and ice[ni][nj]:
                    cnt += 1

            if cnt <= 2:
                new_ice[i][j] = max(0, ice[i][j]-1)
            else:
                new_ice[i][j] = ice[i][j]

    return new_ice

# 얼음 세기
def count_ice():
    cnt = 0
    for i in range(2**N):
        cnt += sum(ice[i])

    return cnt

# 덩어리 파악
def bfs(si,sj, visited):
    queue = collections.deque()
    queue.append([si,sj])
    visited[si][sj] = True
    result = [[si,sj]]

    while queue:
        i, j = queue.popleft()

        for k in range(4):
            ni = i + drc[k][0]
            nj = j + drc[k][1]

            if is_valid(ni,nj) and ice[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = True
                result.append([ni,nj])
                queue.append([ni,nj])


    return len(result)



# 덩어리 세기
def count_cluster():
    visited = [[False] * (2**N) for _ in range(2**N)]
    result = 0

    for i in range(2**N):
        for j in range(2**N):
            if visited[i][j] or not ice[i][j]:
                continue
            result = max(result, bfs(i, j, visited))

    return result


for i in range(Q):
    ice = spin_90(LS[i])
    ice = melting()


print(count_ice())
print(count_cluster())





