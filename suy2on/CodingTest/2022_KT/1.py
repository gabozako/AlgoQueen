
import collections

def solution(levels):
    answer = []
    node_by_level = collections.defaultdict(int)

    for lev in levels:
        node_by_level[lev] += 1

    delete = 0
    add = 0

    ## 루트노드 하나인지
    if not node_by_level[1]:
        add += 1
        node_by_level[1] = 1
    elif node_by_level[1] != 1:
        delete = node_by_level[1] - 1
        node_by_level[1] = 1

    ## 모든 레벨에 노드가 있는지
    for lev in range(sorted(node_by_level.keys())[-1],1,-1):
        # 해당 레벨에서 가질 수 있는 노드 초과하는 경우
        if node_by_level[lev] > 2 ** (lev-1):
            delete = node_by_level[lev] - (2 ** (lev-1))
            node_by_level[lev] = 2 ** (lev-1)

        # 해당 레벨이 이전 레벨 커버 가능한지
        if node_by_level[lev] > node_by_level[lev-1] * 2:
            diff = node_by_level[lev] - (node_by_level[lev-1] * 2)
            if diff % 2 == 1:
                diff += 1
            add += diff // 2
            node_by_level[lev-1] += diff // 2




    return [delete,add]