from typing import List
import collections


def solution(queries: List[List[int]]) -> int:
    answer = 0
    arr_len = collections.defaultdict(int)
    cur_arr_len = collections.defaultdict(int)

    def find_len(capacity):
        i = 0
        while 2 ** i < capacity:
            i += 1

        return 2 ** i

    for arr, inst in queries:
        # 초과하는 경우
        if cur_arr_len[arr] + inst > arr_len[arr]:
            arr_len[arr] = find_len(cur_arr_len[arr] + inst)
            answer += cur_arr_len[arr]

        cur_arr_len[arr] += inst

    return answer