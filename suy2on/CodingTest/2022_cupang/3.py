import collections

drc = [[0,1],[1,0],[0,-1],[-1,0]]
R, C = 0, 0

def is_valid(i,j):
    if 0 <= i <= R-1 and 0 <= j <= C-1:
        return True

    return False

# 물에 잠구는 BFS
def under_water_bfs(sr,sc,grid,water,status,visited):
    queue = collections.deque()
    visited[sr][sc] = True

    # 수위보다 낮으면
    if grid[sr][sc] <= water:
        queue.append([sr,sc])
        status[sr][sc] = False

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + drc[i][0]
            nc = c + drc[i][1]
            if is_valid(nr,nc) and not visited[nr][nc]:
                visited[nr][nc] = True
                if grid[nr][nc] <= water:
                    queue.append([nr,nc])
                    status[nr][nc] = False





# 물에 잠구기
def under_water(grid,water):
    # 방문여부
    visited = [[False] * C for _ in range(R)]
    # 잠긴여부
    status = [[True] * C for _ in range(R)]

    # 외곽부터
    for c in range(C):
        if not visited[0][c]:
            under_water_bfs(0,c,grid,water,status,visited)

    for c in range(C):
        if not visited[R-1][c]:
            under_water_bfs(R-1,c,grid,water,status,visited)

    for r in range(R):
        if not visited[r][0]:
            under_water_bfs(r,0,grid,water,status,visited)

    for r in range(R):
        if not visited[r][C-1]:
            under_water_bfs(r,C-1,grid,water,status,visited)

    return status

# cluster세는 BFS
def cnt_cluster_bfs(sr,sc,visited,status):
    queue = collections.deque()
    visited[sr][sc] = True
    queue.append([sr,sc])

    while queue:
        r,c = queue.popleft()

        for i in range(4):
            nr = r + drc[i][0]
            nc = c + drc[i][1]
            if is_valid(nr,nc) and not visited[nr][nc] and status[nr][nc]:
                visited[nr][nc] = True
                queue.append([nr,nc])

# cluster세기
def cnt_cluster(status):
    # 방문여부
    visited = [[False] * C for _ in range(R)]
    cnt = 0

    for i in range(R):
        for j in range(C):
            if not visited[i][j] and status[i][j]:
                cnt_cluster_bfs(i,j,visited,status)
                cnt += 1

    return cnt


def solution(grid):
    global R,C

    answer = 0
    R = len(grid)
    C = len(grid[0])

    heights = []
    for g in grid:
        heights.extend(g)

    # 섬모양이 바뀌는 고도 오름차순
    heights = sorted(set(heights))

    for h in heights:
        status = under_water(grid,h)
        cnt = cnt_cluster(status)
        # 섬이 두개면 그만
        if cnt == 2:
            return h