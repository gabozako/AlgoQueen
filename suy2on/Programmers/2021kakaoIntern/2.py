# 맨해튼 거리 = 2 안으로는 앉을 수 없음
# 파티션으로 막혀있다면 가능
# P, O, X -> 지켰으면 1, 아니면 0
import collections


def solution(places):
    answer = []
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]

    # 인덱스 범위검사
    def is_valid(r, i, j):
        if 0 <= i <= 4 and 0 <= j <= 4 and places[r][i][j] != "X":
            return True
        return False

    # 거리두기 준수하는지
    def is_obey(room, i, j):
        queue = collections.deque()
        queue.append([i, j, 2])
        dij = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited[room][i][j] = True

        while queue:
            x, y, cnt = queue.popleft()

            # 방문했거나
            if not cnt:
                continue

            # 다음 길 찾아가기
            for k in range(4):
                nx = x + dij[k][0]
                ny = y + dij[k][1]
                # 방문안한곳
                if is_valid(room, nx, ny) and not visited[room][nx][ny]:
                    if places[room][nx][ny] == "P":
                        return False
                    else:
                        visited[room][nx][ny] = True
                        queue.append([nx, ny, cnt - 1])

        return True

    for i in range(5):
        obey = 1
        for j in range(5):
            for k in range(5):
                # 사람이 있는데 사람 규칙이 지켜지지 않았으면 탐색 끝
                if places[i][j][k] == "P" and not is_obey(i, j, k):
                    obey = 0
                    break
            if not obey:
                break
        answer.append(obey)

    return answer