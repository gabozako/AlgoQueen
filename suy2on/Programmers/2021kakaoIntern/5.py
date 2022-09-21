import collections
import itertools

def solution(k, num, links):
    answer = float('inf')
    lines = []
    paths = collections.defaultdict(list)

    def traffic():
        visited = [False] * len(num)
        result = []

        for i in range(len(num)):
            queue = collections.deque()
            queue.append(i)
            visited[i] = True
            cnt = num[i]

            while queue:
                node = queue.popleft()

                for nnode in paths[node]:
                    if not visited[nnode]:
                        visited[nnode] = True
                        cnt += num[nnode]
                        queue.append(nnode)

            result.append(cnt)

        return max(result)


    # 연결사항저장
    for i,link in enumerate(links):
        l, r = link

        if l != -1:
            lines.append([i, l])
            paths[i].append(l)
            paths[l].append(i)

        if r != -1:
            lines.append([i, r])
            paths[i].append(r)
            paths[r].append(i)


    for combi in itertools.combinations(lines,k-1):
        # 지우고
        for c in combi:
            paths[c[0]].remove(c[1])
            paths[c[1]].remove(c[0])

        # 갱신
        answer = min(answer,traffic())

        # 북구
        for c in combi:
            paths[c[0]].append(c[1])
            paths[c[1]].append(c[0])

    return answer

