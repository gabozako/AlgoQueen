import collections

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    chars1 = collections.defaultdict(int)
    chars2 = collections.defaultdict(int)
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            chars1[str1[i:i + 2]] += 1

    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            chars2[str2[i:i + 2]] += 1

    n = set(chars1.keys()) & set(chars2.keys())
    u = set(chars1.keys()) | set(chars2.keys())

    n_score = 0
    u_score = 0
    for c in n:
        n_score += min(chars1[c], chars2[c])

    for c in u:
        u_score += max(chars1[c], chars2[c])

    if not n_score and not u_score:
        return 1 * 65536

    return (n_score * 65536) // u_score