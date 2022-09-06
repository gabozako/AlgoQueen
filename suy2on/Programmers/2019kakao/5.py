## recursion 제한풀기, 메모리초과(배열로했을때)
import collections
import bisect
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, val=0, xy=None, left=None, right=None):
        self.val = val
        self.xy = xy
        self.left = left
        self.right = right


def solution(nodeinfo):
    root = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))[0]
    sortedInf = sorted(nodeinfo)
    sx = [n[0] for n in sortedInf]

    # 트리잇기
    queue = collections.deque()
    root = Node(nodeinfo.index(root) + 1, root)
    queue.append([-1, 100001, root])

    while queue:
        left, right, node = queue.popleft()
        # 왼쪽자식
        ll = bisect.bisect_right(sx, left)
        lr = bisect.bisect_left(sx, node.xy[0])
        if ll < lr:
            ln = sorted(sortedInf[ll:lr], key=lambda x: -x[1])[0]
            ln = Node(nodeinfo.index(ln) + 1, ln)
            node.left = ln
            queue.append([left, node.xy[0], ln])
        # 오른쪽자식
        rl = bisect.bisect_right(sx, node.xy[0])
        rr = bisect.bisect_left(sx, right)
        if rl < rr:
            rn = sorted(sortedInf[rl:rr], key=lambda x: -x[1])[0]
            rn = Node(nodeinfo.index(rn) + 1, rn)
            node.right = rn
            queue.append([node.xy[0], right, rn])

    # 트리출력
    result1 = []
    result2 = []

    def pre(node):
        if not node:
            return
        result1.append(node.val)
        pre(node.left)
        pre(node.right)

    def pro(node):
        if not node:
            return
        pro(node.left)
        pro(node.right)
        result2.append(node.val)

    pre(root)
    pro(root)
    answer = []
    answer.append(result1)
    answer.append(result2)

    return answer