"""
Joe's implementation
"""

def countGroups(related):
    """
    input: a list of strings of binary digits
    output: an integer

    countGroups(['1100', '1110', '0110', '0001'])
    """
    unvisited = dict(zip(range(len(related)), [True for x in related]))
    visited = dict(zip(range(len(related)), [False for x in related]))

    makeKnownLists = lambda x: [k for k, v in enumerate(x) if int(v) == 1]
    knownLists = list(map(makeKnownLists, related))
    groupCount = 0

    print(f'unvisited {unvisited}')
    print(f'knownLists {knownLists}')

    for person in unvisited.keys():
        pivot = person

        if visited[pivot]:
            continue

        while isinstance(pivot, int):

            print("Current pivot: {}".format(pivot))
            unvisited[pivot], visited[pivot] = False, True
            knownList = knownLists[pivot]
            print("visited: {}".format(visited))
            print("knownList of person {}: {}".format(pivot, knownList))

            for known in knownList:
                if visited[known]:
                    pivot = None
                    continue
                else:
                    unvisited[known], visited[known] = False, True
                    pivot = known
                    knownList = knownLists[pivot]
                    print("visited: {}".format(visited))
                    print("knownList of {}: {}".format(pivot, knownList))
                    break
        groupCount += 1
        print(groupCount)
    return groupCount
    
a = countGroups(['10110', '01010', '10110', '11110', '00001'])
print(a)