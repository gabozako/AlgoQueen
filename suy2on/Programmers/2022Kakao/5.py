import collections


def find_path(info, paths):
    result = 0
    queue = collections.deque()
    queue.append(([0], 1, 0))

    while queue:
        nodes, sheep, wolf = queue.popleft()
        result = max(result, sheep)

        for node in nodes:
            for neighbor in paths[node]:
                if neighbor not in nodes:
                    if info[neighbor] and sheep - wolf < 2:  # 늑대가 추가 안되는 경우
                        continue
                    newNodes = nodes[:]
                    newNodes.append(neighbor)
                    if info[neighbor]:  # 늑대면
                        queue.append((newNodes, sheep, wolf + 1))
                    else:  # 양이면
                        queue.append((newNodes, sheep + 1, wolf))

    return result


def solution(info, edges):
    paths = collections.defaultdict(list)
    # 각 연결노드 저장
    for edge in edges:
        paths[edge[0]].append(edge[1])
        paths[edge[1]].append(edge[0])

    return find_path(info, paths)