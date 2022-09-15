### [3차] 자동완성


class Node:
    def __init__(self, char):
        self.char = char
        self.cnt = 1
        self.children = {}


def solution(words):
    answer = 0

    # 트라이만들기
    root = Node("!")
    for w in words:
        p = root
        for c in w:
            if c in p.children.keys():
                p.children[c].cnt += 1
            else:
                p.children[c] = Node(c)
            p = p.children[c]

    # 검색
    for w in words:
        p = root
        cnt = 0
        for c in w:
            p = p.children[c]
            cnt += 1
            if p.cnt == 1:
                break

        answer += cnt

    return answer