# 정확성
def solution(words, queries):
    answer = []
    words = set(words)  # 중복제거

    for q in queries:
        cnt = 0
        l = len(q)
        if q[0] == "?":
            while "?" in q:
                q = q.replace("?", "")
            for w in words:
                if len(w) == l and w[-len(q):] == q:
                    cnt += 1
        else:
            while "?" in q:
                q = q.replace("?", "")
            for w in words:
                if len(w) == l and w[:len(q)] == q:
                    cnt += 1

        answer.append(cnt)

    return answer


### 트라이
import sys

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self, char, children, end):
        self.char = char
        self.children = children
        self.end = end


cnt = 0

def solution(words, queries):
    # 중복제거
    words = set(words)

    # 트라이 두개 만들기
    trie1 = Node(None, dict(), False)
    trie2 = Node(None, dict(), False)

    for word in words:
        p1 = trie1
        p2 = trie2
        for ch in word:
            if ch not in p1.children:
                p1.children[ch] = Node(ch, {}, False)
            p1 = p1.children[ch]
        p1.end = True

        for ch in word[::-1]:
            if ch not in p2.children:
                p2.children[ch] = Node(ch, {}, False)
            p2 = p2.children[ch]
        p2.end = True


    # 트라이 탐색하면서 가능한 단어 개수 세기

    def dfs1(p, query, i):
        global cnt

        if i == len(query):  # 길이 만큼 탐색 끝나면
            if p.end:
                cnt += 1
            return

        for ch in p.children.keys():
            if query[i] != "?" and query[i] == ch or query[i] == "?":
                dfs1(p.children[ch], query, i + 1)

    def dfs2(p, query, i):
        global cnt

        if i == -1:  # 길이 만큼 탐색 끝나면
            if p.end:
                cnt += 1
            return

        for ch in p.children.keys():
            if query[i] != "?" and query[i] == ch or query[i] == "?":
                dfs2(p.children[ch], query, i - 1)

    answer = []
    for q in queries:
        global cnt
        cnt = 0
        if q[0] == "?":
            dfs2(trie2, q, len(q)-1)
        else:
            dfs1(trie1, q, 0)
        answer.append(cnt)

    return answer


## 이분탐색 

from bisect import bisect_left, bisect_right


def count_value(a, left, right):
    left_index = bisect_left(a, left)
    right_index = bisect_right(a, right)
    return right_index - left_index


def solution(words, queries):
    answer = []

    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]


    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_value(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_value(reverse_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer




