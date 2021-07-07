graph1 = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F", "G"], "D": ["I", "J"], "E": [], "F": [], "G": [],
          "I": ["K", "L"], "J": [], "K": [], "L": []}
graph2 = graph1.copy()

CLOSED = []
goal = "J"
nodes = list(graph1.keys())
start = nodes[0]

def goalTest(OPENgraph1, OPENgraph2):
    for i in OPENgraph1:
        for j in OPENgraph2:
            if i == j:
                print("Goal found")
                break
    return "interseact"


"""
def REPORT(current):
    OPEN = [start]
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
            children = graph1.get(current)
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
"""
