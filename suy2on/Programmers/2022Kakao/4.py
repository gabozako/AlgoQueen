## 조건에 맞는 소수 구하기
import collections


def make_k(n, k):
    result = ""
    while n >= k:
        result = str(n % k) + result
        n = n // k

    result = str(n) + result
    return result

## 소수 구할때 제곱근 기준 아래로만 구하기
def is_prime(number):
    if number == 1:
        return False

    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1

    return True


def solution(n, k):
    answer = 0

    k_number = make_k(n, k)  # k진수로 만들기
    maybeAnswer = k_number.split("0")

    for num in maybeAnswer:
        if num and is_prime(int(num)):
            answer += 1

    return answer


print(make_k(1000000,2))