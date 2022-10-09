import collections
import heapq


def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    # Write your code here
    paths = collections.defaultdict(list)

    for f, t, w in zip(g_from, g_to, g_weight):
        paths[f].append([t, w])
        paths[t].append([f, w])

    def shortcut(start, end):
        costs = [float('inf')] * (g_nodes + 1)
        pq = []
        heapq.heappush(pq, [0, start])
        costs[start] = 0

        while pq:
            c, node = heapq.heappop(pq)

            if node == end:
                return c

            for nnode, w in paths[node]:
                if costs[nnode] > c + w:
                    costs[nnode] = c + w
                    heapq.heappush(pq, [c + w, nnode])

    return shortcut(1, x) + shortcut(x, y) + shortcut(y, g_nodes)