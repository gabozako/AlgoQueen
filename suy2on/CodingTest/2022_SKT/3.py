import collections
import sys

sys.setrecursionlimit(10 ** 6)

class Node:
    def __init__(self, ch, end=False):
        self.ch = ch
        self.end = end
        self.children = {}


def solution(s, word_dict):
    answer = []

    # 사전 트라이로 정리
    root = Node("!")
    for word in word_dict:
        p = root
        for ch in word:
            if ch not in p.children.keys():
                p.children[ch] = Node(ch)
            p = p.children[ch]
        p.end = True



    def dfs(substr, cnt):
        if len(substr) == 1:
            answer.append(cnt)
            return

        p = root
        for i in range(len(substr)):
            # 사전에서 더이상 단어가 없으면
            if substr[i] not in p.children.keys():
                break
            p = p.children[substr[i]]
            # 사전에 단어가 있으면
            if p.end:
                dfs(substr[i:], cnt+1)

    dfs(s,0)

    return max(answer)