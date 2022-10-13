## 스타트 택시
import sys
import collections
input = sys.stdin.readline

N, M, F = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

ti, tj = map(lambda x : int(x)-1 , input().split())

# 승객
passenger = []
for _ in range(M):
    passenger.append(list(map(lambda x: int(x) - 1, input().split())))



def is_valid(i,j):
    if 0<= i <= N-1 and 0 <= j <= N-1 and not board[i][j]:
        return True
    return False

drc = [[0,1],[0,-1],[1,0],[-1,0]]

# 최단거리 거리 모두 구해놓기
short_cut = [[[[float('inf')] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]

for si in range(N):
    for sj in range(N):
        queue = collections.deque()
        queue.append([si,sj,0])
        short_cut[si][sj][si][sj] = 0

        while queue:
            i, j, c = queue.popleft()

            for k in range(4):
                ni = i + drc[k][0]
                nj = j + drc[k][1]
                if is_valid(ni,nj) and short_cut[si][sj][ni][nj] == float('inf'):
                    short_cut[si][sj][ni][nj] = c + 1
                    queue.append([ni,nj,c+1])


# 태울 승객 찾기(끝날 수 있음) + 연료 태우기
def can_drive():
    global F, ti, tj

    who = []
    for idx, p in enumerate(passenger):
        pi, pj, di, dj = p
        who.append([short_cut[ti][tj][pi][pj], pi, pj, di, dj, idx])

    # 승객 고르기
    who.sort(key=lambda x : (x[0],x[1],x[2]))
    distance, pi, pj, di, dj, idx = who[0]

    # 연료 갱신
    F -= (distance + short_cut[pi][pj][di][dj])

    if F < 0:
        return False

    # 승객 삭제 택시 위치 변경 연료 채우기
    ti, tj = di, dj
    del passenger[idx]
    F += short_cut[pi][pj][di][dj] * 2

    return True

while passenger:
    if not can_drive():
        print(-1)
        break

if not passenger:
    print(F)

