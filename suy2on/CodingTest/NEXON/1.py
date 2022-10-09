def minNum(samDaily, kellyDaily, difference):
    # Write your code here
    if samDaily >= kellyDaily:
        return -1
    diff = kellyDaily - samDaily

    return difference // diff + 1
