import collections


def solution(n, roads, sources, destination):
    answer = []
    paths = collections.defaultdict(list)
    toDestination = [-1] * (n + 1)

    # 인접노드기록
    for n1, n2 in roads:
        paths[n1].append(n2)
        paths[n2].append(n1)

    # 도착지를 기준으로 모든 거리 계산
    def toDest():
        visited = [False] * (n + 1)
        queue = collections.deque()
        queue.append([destination, 0])
        visited[destination] = True
        toDestination[destination] = 0

        while queue:
            node, cost = queue.popleft()
            for nnode in paths[node]:
                if not visited[nnode]:
                    toDestination[nnode] = cost + 1
                    visited[nnode] = True
                    queue.append([nnode, cost + 1])

    toDest()

    for source in sources:
        answer.append(toDestination[source])

    return answer