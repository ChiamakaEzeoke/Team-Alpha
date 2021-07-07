myTree = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": ["I", "J"], "E": [""], "F": [], "G": [],
          "I": ["K", "L"], "J": [], "K": [], "L": []}
goal = "J"
nodes = list(myTree.keys())
CLOSED = []
start = nodes[0]
OPEN = [start]

def REPORT(current):
    global OPEN
    global CLOSED
    result = "SUCCESS"
    while (len(OPEN) != 0):
        if current == goal:
            print(result)
            break
        else:
            print(OPEN)
            OPEN.remove(current)
            CLOSED.append(current)
            print("CLOSED: ", CLOSED)
            children = myTree.get(current)
            #put children of current into OPEN
            OPEN = OPEN + children
            print("FAILURE")
            #remove the first element
            current = OPEN[0]
            print(current)
            if result != "SUCCESS":
                REPORT(current)
    return OPEN
REPORT(start)
