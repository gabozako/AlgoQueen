P, N = map(int, input().split())
piros = list(map(int, input().split()))
if P == 200:
    print(0)
else:
    piros.sort()

    for i in range(N):
        P += piros[i]
        if P >= 200:
            print(i + 1)
            break

    if P < 200:
        print(N)
