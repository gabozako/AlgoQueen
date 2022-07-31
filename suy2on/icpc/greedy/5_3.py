## 설탕배달
N = int(input())

for i in range(N//5+1):
    mod = N - 5 * (N//5 - i)
    div3, mod = divmod(mod,3)

    if not mod:
        print(div3 + N//5 - i)
        exit(0)

print(-1)

