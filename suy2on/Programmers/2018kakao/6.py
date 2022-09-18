def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        binary = bin(i | j)[2:]
        binary = binary.zfill(n)
        binary = binary.replace("1", "#")
        binary = binary.replace("0", " ")
        answer.append(binary)

    return answer