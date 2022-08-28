import bisect
import itertools

answer = float('inf')


def solution(n, weak, dist):

    def dfs(num, cover, pos, dis):
        global answer

        if cover >= len(weak):  # 커버 완료
            answer = min(answer, num)
            return

        if num >= len(dis):  # 커버할 수 없는 경우
            return

        np = weak[pos] + dis[num]

        tail = bisect.bisect_right(weak, np % n)  # 삽입위치찾기
        if tail >= len(weak):  # 삽입위치가 맨 뒤일때
            tail = 0

        if tail <= pos:  # 삽입위치 앞으로 돌아왔을때
            dfs(num + 1, cover + tail + len(weak) - pos, tail, dis)
        else:
            dfs(num + 1, cover + tail - pos, tail, dis)

    for permu in itertools.permutations(dist):
        for i in range(len(weak)):
            dfs(0, 0, i, permu)

    if answer == float('inf'):
        return -1

    return answer