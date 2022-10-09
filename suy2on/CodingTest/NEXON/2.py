def getMaximumRemovals(order, source, target):
    # Write your code here
    source = list(source)
    answer = 0
    while answer < len(order):
        source[order[answer] - 1] = "-"
        scan_source = "".join(source)

        p = 0
        contain = False
        for c in scan_source.replace("-", ""):
            if target[p] == c:
                p += 1
            if p == len(target):
                contain = True
                break

        if not contain:
            return answer

        answer += 1

    return answer