numbers = [
    "111101101101111",
    "110010010010111",
    "111001111100111",
    "111001111001111",
    "101101111001001",
    "111100111001111",
    "111100111101111",
    "111101001001001",
    "111101111101111",
    "111101111001111"
]

def solution(pixels):
    answer = ''
    n = len(pixels[0]) // 3

    for i in range(n):
        num = ""
        # 숫자 추출
        for pixel in pixels:
            num += pixel[i*3:i*3+3]
        # 숫자 매칭해서 더하기
        answer += str(numbers.index(num))
    return answer