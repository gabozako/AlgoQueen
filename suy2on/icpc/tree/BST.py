## Binary Search Tree
import sys

input = sys.stdin.readline


def getLeft(i):
    return i * 2


def getRight(i):
    return i * 2 + 1


def getParent(i):
    return i // 2


trees = {}

values = []

while True:
    try:
        values.append(int(input()))
    except:
        break


def pre(idx):
    if idx not in trees.keys():
        trees[idx] = values.pop(0)

    if values and values[0] < trees[idx]:
        pre(getLeft(idx))

    if idx == 1:
        if values and trees[idx] < values[0]:
            pre(getRight(idx))
    else:
        if values and trees[idx] < values[0] < trees[getParent(idx)]:
            pre(getRight(idx))


def post(idx):
    if idx not in trees.keys():
        return

    post(getLeft(idx))
    post(getRight(idx))
    print(trees[idx])


pre(1)
post(1)
