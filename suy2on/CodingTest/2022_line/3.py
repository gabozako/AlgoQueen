from typing import List


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    answer = [[0] * (n) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 온도 상승 계산
            for fire in fires:
                di = abs(i - fire[0])
                dj = abs(j - fire[1])
                if di == dj == 0:
                    answer[i - 1][j - 1] += m
                else:
                    answer[i - 1][j - 1] += max(0, m - (max(di, dj) - 1))

            # 온도 하강 계산
            for ice in ices:
                di = abs(i - ice[0])
                dj = abs(j - ice[1])
                if di + dj == 0:
                    answer[i - 1][j - 1] -= m
                else:
                    answer[i - 1][j - 1] -= max(0, m - (di + dj - 1))

    return answer