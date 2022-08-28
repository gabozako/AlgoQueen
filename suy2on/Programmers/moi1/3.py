import collections


def solution(grid):
    answer = []
    R = len(grid)
    C = len(grid[0])
    # 왼, 오, 위, 아래
    dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    next_dir = [{"L": 3, "R": 2, "S": 0}, {"L": 2, "R": 3, "S": 1}, {"L": 0, "R": 1, "S": 2}, {"L": 1, "R": 0, "S": 3}]

    visited = [[[False] * 4 for _ in range(C)] for _ in range(R)]

    def bfs(start, direction):
        # 이미 방문했다면 멈추기
        if visited[start[0]][start[1]][direction]:
            return

        queue = collections.deque()
        visited[start[0]][start[1]][direction] = True

        # 다음 node
        nr = (start[0] + dirs[direction][0]) % R
        nc = (start[1] + dirs[direction][1]) % C

        queue.append([1, [nr, nc], direction])

        while queue:
            c, node, dirt = queue.popleft()

            # 새로운 방향
            nd = next_dir[dirt][grid[node[0]][node[1]]]
            drc = dirs[nd]
            # 방문하지 않은 경우
            if not visited[node[0]][node[1]][nd]:
                nr = (node[0] + drc[0]) % R
                nc = (node[1] + drc[1]) % C
                visited[node[0]][node[1]][nd] = True
                queue.append([c + 1, [nr, nc], nd])
            else:  # 방문한경우
                if node == start and nd == direction: # 처음으로 발견된 순환이면
                    answer.append(c)
                else: # 이전에 발견된 순환이면
                    return

    for i in range(R):
        for j in range(C):
            for d in range(4):
                bfs([i,j],d)

    return sorted(answer)

print(solution(["R","R"]))