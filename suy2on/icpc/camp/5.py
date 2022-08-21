import sys
import collections

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
chars = input().rstrip()

paths = collections.defaultdict(list)
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    paths[n1].append([chars[n2-1], n2])
    paths[n2].append([chars[n1-1], n1])

for path in paths.values():
    path.sort(reverse=True)


answer = ""

def dfs(node,  name, parent):
    global answer

    if (len(paths[node[1]]) == 1 and paths[node[1]][0][1] == parent) or len(paths[node[1]]) == 0:
        if answer < name:
            answer = name
        return

    ch = ""
    for i, child in enumerate(paths[node[1]]):
        if child[1] != parent:
            if not ch:
                ch = child[0]
                dfs(child, name + child[0], node[1])
            else:
                if ch == child[0]:
                    dfs(child, name + child[0], node[1])
                else:
                    break




dfs([chars[0], 1], chars[0], 0)
print(answer)


