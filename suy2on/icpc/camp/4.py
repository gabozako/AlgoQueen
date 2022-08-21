N = int(input())
skills = input()

connect = {"S":0, "K":0, "L":0, "R":0}
cnt = 0
for skill in skills:
    if "1"<= skill <= "9":
        cnt += 1
    else:
        connect[skill] += 1
        if connect["S"] < connect["K"] or connect["L"] < connect["R"]:
            break

print(cnt + min(connect["S"], connect["K"]) + min(connect["L"], connect["R"]))






