import collections


def solution(id_list, report, k):
    answer = []
    mails = collections.defaultdict(int)
    black_list = collections.defaultdict(set)

    for r in report:
        mem1, mem2 = r.split()
        black_list[mem2].add(mem1)

    for b in black_list.keys():
        if len(black_list[b]) >= k:
            for mem in black_list[b]:
                mails[mem] += 1

    return [mails[i] for i in id_list]