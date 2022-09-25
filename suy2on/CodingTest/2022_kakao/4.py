import collections

def to_binary(num):
    result = ""

    while num >= 2:
        num, mod = divmod(num, 2)
        result = str(mod) + result

    return str(num) + result

def zero_fill(binary):
    i = 0
    total = 2 ** 0
    while len(binary) > total:
        i += 1
        total += (2 ** i)


    return binary.zfill(total)

def can_make_tree(sub_tree):

    # 마지막 노드
    if len(sub_tree) == 1:
        if sub_tree[0] == "0":
            return 0
        else:
            return 1

    mid = (len(sub_tree) - 1) // 2

    # 루트노드가 없을 때
    if sub_tree[mid] == "0":
        if can_make_tree(sub_tree[:mid]) == 0 and can_make_tree(sub_tree[mid+1:]) == 0:
            return 0
        else:
            return -1
    # 루트노드 있을 때
    else:
        if can_make_tree(sub_tree[:mid]) != -1 and can_make_tree(sub_tree[mid+1:]) != -1:
            return 1
        else:
            return -1



def solution(numbers):
    answer = []
    for number in numbers:
        # 이진수로 만들기
        binary = to_binary(number)
        # 포화이진트리 만들기
        binary = zero_fill(binary)
        # 길이 1일 때
        if len(binary) == 1:
            answer.append(int(binary))
        else:
            if can_make_tree(binary) == 1:
                answer.append(1)
            else:
                answer.append(0)


    return answer