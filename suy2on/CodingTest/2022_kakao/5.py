class Node:
    def __init__(self, val = "EMPTY"):
        self.val = val
        self.parent = None
        self.children = []

def solution(commands):
    answer = []

    table = [[Node() for _ in range(50)] for _ in range(50)]
    managed = set()

    for command in commands:
        print("_____")
        for i in range(4):
            for j in range(4):
                target = table[i][j]
                while target.parent:
                    target = target.parent
                print(target.val)

        command = command.split()

        if command[0] == "PRINT":
            r, c = int(command[1]), int(command[2])
            target = table[r - 1][c - 1]
            while target.parent:
                target = target.parent
            answer.append(target.val)


        elif command[0] == "UPDATE":
            if len(command) == 4:
                r, c, val = int(command[1]), int(command[2]), command[3]
                target = table[r-1][c-1]
                while target.parent:
                    target = target.parent
                target.val = val
                managed.add(target)
            else:
                val1, val2 = command[1], command[2]
                # for i in range(50):
                #     for j in range(50):
                #         target = table[i][j]
                #         while target.parent:
                #             target = target.parent
                #         if target.val == val1:
                #             target.val = val2
                for node in managed:
                    if node.val == val1:
                        node.val = val2


        elif command[0] == "MERGE":
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            target1 = table[r1-1][c1-1]
            while target1.parent:
                target1 = target1.parent

            target2 = table[r2 - 1][c2 - 1]
            while target2.parent:
                target2 = target2.parent

            if target1.val != "EMPTY":
                if target1.children:
                    if target2.children:
                        for child in target2.children:
                            child.parent = target1
                            target1.children.append(child)
                    else:
                        target1.children.append(target2)
                        target2.parent = target1

                else:
                    parent = Node(target1.val)
                    if target2.children:
                        for child in target2.children:
                            parent.children.append(child)
                            child.parent = parent
                    else:
                        parent.children.append(target2)
                        target2.parent = parent
                    parent.children.append(target1)
                    target1.parent = parent
            else:
                if target2.children:
                    if target1.children:
                        for child in target1.children:
                            child.parent = target2
                            target2.children.append(child)

                    else:
                        target2.children.append(target1)
                        target1.parent = target2
                else:
                    parent = Node(target2.val)
                    if target1.children:
                        for child in target1.children:
                            child.parent = parent
                            parent.children.append(child)
                    else:
                        parent.children.append(target1)
                        target1.parent = parent
                    parent.children.append(target2)
                    target2.parent = parent

        else:
            r, c = int(command[1]), int(command[2])
            target = table[r-1][c-1]
            while target.parent:
                target = target.parent

            for child in target.children:
                child.val = "EMPTY"
                child.parent = None

            if target.val != "EMPTY":
                table[r-1][c-1].val = target.val

    print("_____")
    for i in range(2):
        for j in range(2):
            target = table[i][j]
            while target.parent:
                target = target.parent
            print(target.val)


    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
# print(solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))