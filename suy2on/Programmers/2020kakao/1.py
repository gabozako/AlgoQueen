def solution(s):
    mid = len(s) // 2
    # 문자열 길이 1일 때
    if not mid:
        return 1

    answer = float('inf')

    # 문자열 간격 최대는 mid
    for i in range(1, mid + 1):
        limit = len(s) // i
        j = 0
        result = ""
        # 문자열 limit까지 돌기
        while j <= i * (limit - 1):

            cnt = 1
            # 중복문자열 수 세기
            while j < i * (limit - 1) and s[j:j + i] == s[j + i:j + 2 * i]:
                cnt += 1
                j += i

            # 문자열 붙이기
            if cnt == 1:
                result += s[j:j + i]
            else:
                result += str(cnt) + s[j:j + i]

            j += i

        # 나머지 붙이기
        result += s[j:]
        answer = min(answer, len(result))

    return answer
