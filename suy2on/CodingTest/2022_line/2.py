from typing import List
import collections


def solution(k: int, dic: List[str], chat: str) -> str:
    answer = []

    chats = chat.split()

    for chat in chats:
        bw = False
        freqs = dict(collections.Counter(chat))
        head = chat.replace(".", "a")
        tail = chat.replace(".", "z" * k)
        for d in dic:
            # 일치
            if chat == d:
                bw = True
                break

            if len(head) <= len(d) <= len(tail) and head <= d <= tail:
                check = True
                for key in freqs.keys():
                    if key != "." and freqs[key] > d.count(key):
                        check = False
                if check:
                    bw = True
                    break

        if bw:
            answer.append("#" * len(chat))
        else:
            answer.append(chat)

    return " ".join(answer)
