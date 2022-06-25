# R행 C열
# 네 방향중 하나로 인접한 미네랄이 포한된 두 칸은 같은 클러스터
# 창영 : 왼쪽 / 상근 : 오른쪽 -> 번갈아가며 막대기 던짐 => 2로 나눈 나머지로 차례구분
# 막대기를 던질 높이 주어짐 -> 막대기가 미네랄을 만나면 파괴한뒤 멈춘다
# 파괴후 : 클러스터가 공중에 뜨는경우 바닥으로 떨어짐 -> 다른클러스터나 땅을 만나면 멈춤  => 하나의 클러스터만 떨어짐
import sys
import collections

input = sys.stdin.readline

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
visited = [[0] * C for _ in range(R)]
mine = []

for _ in range(R):
    mine.append(list(input().rstrip()))

N = int(input())
heights = list(map(int, input().split()))  # 던지는 높이


## 유효한 좌표
def is_valid(r, c):
    if 0 <= r <= R - 1 and 0 <= c <= C - 1:
        return True
    else:
        return False


## 방문기록 초기화
def init_visited():
    for i in range(R):
        for j in range(C):
            visited[i][j] = 0


## 막대던져서 부셨는지
def is_hit(height, i):
    if i % 2:  # 홀수 -> 오른쪽
        for p in range(C - 1, -1, -1):
            if mine[R - height][p] == 'x':
                mine[R - height][p] = '.'
                return True
    else:
        for p in range(0, C):
            if mine[R - height][p] == 'x':
                mine[R - height][p] = '.'
                return True

    return False


## bfs탐색
def bfs(i,j):
    cluster = []
    queue = collections.deque()
    queue.append([i,j])

    while queue:
        r, c = queue.popleft()
        if mine[r][c] == 'x' and not visited[r][c]:
            visited[r][c] = 1
            cluster.append([r,c])
            for j in range(4):
                rr = r + dr[j]
                cc = c + dc[j]
                if is_valid(rr, cc):
                    queue.append([rr, cc])

    return cluster

# 클러스터들 bfs로 쭉 찾기
def detect_cluster():
    clusters = []
    for i in range(R):
        for j in range(C):
            if mine[i][j] == 'x' and not visited[i][j]:
                clusters.append(bfs(i,j))

    return clusters

# 떠있는 클러스터 찾기 -> 바닥이 포한된 것이 없는 것
def detect_fall_cluster(clusters):
    for cluster in clusters:
        found = True
        for c in cluster:
            if c[0] == R-1:
                found = False
                break
        if found:
            return cluster



# 클러스터 떨어트리기
def drop_cluster(cluster):
    drop = R
    clusterByCol = sorted(cluster, key=lambda x : (x[1],-x[0]))
    bef = clusterByCol[0]
    drop = min(drop, how_much_drop(bef[0],bef[1]))

    # cluster의 열마다 맨 밑 찾기
    for i in range(1,len(clusterByCol)):
        if bef[1] == clusterByCol[i][1]:
            continue
        bef = clusterByCol[i]
        drop = min(drop, how_much_drop(bef[0], bef[1]))

    cluster.sort(reverse=True)
    for c in cluster:
        mine[c[0]][c[1]] = '.'
        mine[c[0]+drop][c[1]] = 'x'

# 얼마나 떨어트릴지 구하기
def how_much_drop(r, c):
    cnt = 0
    for i in range(r + 1, R):
        if mine[i][c] == 'x':
            # print(i)
            break
        cnt += 1
    return cnt

# 실행문
for i in range(N):
    if is_hit(heights[i], i):
        clusters = detect_cluster()
        cluster = detect_fall_cluster(clusters)
        if cluster:
            drop_cluster(cluster)
        init_visited()

for i in range(R):
    print("".join(mine[i]))
