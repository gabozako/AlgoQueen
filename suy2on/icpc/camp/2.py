N = int(input())
phones = list(map(int, input().split()))

totalSomo = 2
somo = 2
prePhone = phones[0]
i = 1
while i < N:
    if prePhone == phones[i]:
        somo = somo * 2
    else:
        somo = 2

    totalSomo += somo
    prePhone = phones[i]

    if totalSomo >= 100: ## 충전필요시
        prePhone = 0
        totalSomo = 0
        somo = 0

    i += 1

print(totalSomo)


