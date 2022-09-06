def solution(n, arr1, arr2):
    answer = []

    def to_bin(num):
        result = bin(num)[2:]

        return "0" * (n - len(result)) + result

    for i in range(n):
        result = ""
        line1 = to_bin(arr1[i])
        line2 = to_bin(arr2[i])

        for j in range(n):
            if line1[j] == line2[j] == "0":
                result += " "
            else:
                result += "#"

        answer.append(result)

    return answer