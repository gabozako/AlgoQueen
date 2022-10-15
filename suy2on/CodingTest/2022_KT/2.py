def solution(replies, n, k):
    answer = []

    def is_good(string):
        # 길이는 n - len(문자열) // k
        for l in range(n, len(string)//k+1):
            for start in range(len(string)-l+1):
                word = string[start:start+l]
                same = 0
                for p in range(start, len(string)-l+1,l):
                    if string[p:p+l] != word:
                        break
                    same += 1
                    # 불량
                    if same >= k:
                        return 0

        return 1

    for reply in replies:
        answer.append(is_good(reply))




    return answer