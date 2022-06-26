N = int(input())

# 1500000주기로 반복
fibo = [0] * 1500000
fibo[0] = 0
fibo[1] = 1

i = 2
limit = min(N+1, 1500000)
while i < limit:
     fibo[i] = (fibo[i-1] + fibo[i-2]) % 1000000
     i += 1



print(fibo[N%1500000])