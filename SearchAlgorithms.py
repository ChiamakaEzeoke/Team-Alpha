import time
from queue import Queue


def DFS(canvas, currentNode, nodeToFind):
    if currentNode.value is nodeToFind.value:
        canvas.create_oval(currentNode.cordinates[0], currentNode.cordinates[1], currentNode.cordinates[2],
                           currentNode.cordinates[3], fill="blue")
        raise Exception("This was meant to happen, don't panic")

    print(currentNode.value)
    canvas.create_oval(currentNode.cordinates[0], currentNode.cordinates[1], currentNode.cordinates[2],
                       currentNode.cordinates[3], fill="red")

    if currentNode.left is None and currentNode.right is None:
        return

    canvas.update()

    time.sleep(1)
    DFS(canvas, currentNode.left, nodeToFind)

    canvas.update()

    time.sleep(1)
    DFS(canvas, currentNode.right, nodeToFind)


def BFS(canvas, currentNode, nodeToFind):
    myQueue = Queue(maxsize=10)

    myQueue.put(currentNode)

    while myQueue.empty() is False:
        topElement = myQueue.get()
        print(topElement.value)
        if topElement.value is nodeToFind.value:
            canvas.create_oval(topElement.cordinates[0], topElement.cordinates[1], topElement.cordinates[2],
                               topElement.cordinates[3], fill="blue")
            break

        canvas.create_oval(topElement.cordinates[0], topElement.cordinates[1], topElement.cordinates[2],
                           topElement.cordinates[3], fill="red")

        canvas.update()

        time.sleep(1)
        if topElement.left is not None: 
            myQueue.put(topElement.left)

        if topElement.right is not None:
            myQueue.put(topElement.right)


def DLS(canvas, currentNode, nodeToFind, currentLevel, maxLevel=2, color="red"):
    if currentLevel > maxLevel:
        return

    if currentNode.value is nodeToFind.value:
        canvas.create_oval(currentNode.cordinates[0], currentNode.cordinates[1], currentNode.cordinates[2],
                           currentNode.cordinates[3], fill="blue")
        raise Exception("This was meant to happen, don't panic")

    print("node - ", currentNode.value, "level - ", currentLevel)
    canvas.create_oval(currentNode.cordinates[0], currentNode.cordinates[1], currentNode.cordinates[2],
                       currentNode.cordinates[3], fill=color)

    if currentNode.left is None and currentNode.right is None:
        return

    canvas.update()

    time.sleep(1)
    DLS(canvas, currentNode.left, nodeToFind, currentLevel + 1, maxLevel, color)

    canvas.update()

    time.sleep(1)
    DLS(canvas, currentNode.right, nodeToFind, currentLevel + 1, maxLevel, color)


def IDFS(canvas, currentNode, nodeToFind, currentLevel):
    stopIteration = False
    maxLevel = 0
    colors = ["green", "deep pink", "yellow", "red"]
    while stopIteration is not True:
        color = colors[maxLevel]
        stopIteration = DLS(canvas, currentNode, nodeToFind, currentLevel, maxLevel, color)

        maxLevel = maxLevel + 1


def BDS(canvas, currentNode, nodeToFind):
    searchingDown = Queue(maxsize=10)
    searchingUp = Queue(maxsize=10)
    intersectionFound = False

    searchingDown.put(currentNode)
    searchingUp.put(nodeToFind)

    exploredNodes = []

    while not intersectionFound:

        # Searching down
        topElement = searchingDown.get()
        canvas.create_oval(topElement.cordinates[0], topElement.cordinates[1], topElement.cordinates[2],
                       topElement.cordinates[3], fill="red")

        canvas.update()
        time.sleep(1)
        
        exploredNodes.append(topElement)

        if topElement.head is not None and topElement.head not in exploredNodes:
            searchingDown.put(topElement.head)

        if topElement.left is not None and topElement.left not in exploredNodes:
            searchingDown.put(topElement.left)

        if topElement.right is not None and topElement.right not in exploredNodes:
            searchingDown.put(topElement.right)


        
        # Check for Intersection after searching down
        intersectionList = CheckForIntersection(searchingDown.queue, searchingUp.queue)

        if len(intersectionList) > 0:
            intersectionNode = intersectionList[0]
            canvas.create_oval(intersectionNode.cordinates[0], intersectionNode.cordinates[1], intersectionNode.cordinates[2],
                       intersectionNode.cordinates[3], fill="blue")

            canvas.update()
            time.sleep(1)

            intersectionFound = True
            break

        

        # Searching Up
        topElement = searchingUp.get()
        canvas.create_oval(topElement.cordinates[0], topElement.cordinates[1], topElement.cordinates[2],
                       topElement.cordinates[3], fill="red")

        canvas.update()
        time.sleep(1)

        exploredNodes.append(topElement)

        if topElement.head is not None and topElement.head not in exploredNodes:
            searchingUp.put(topElement.head)

        if topElement.left is not None and topElement.left not in exploredNodes:
            searchingUp.put(topElement.left)

        if topElement.right is not None and topElement.right not in exploredNodes:
            searchingUp.put(topElement.right)

        
        # Check for intersection after searching up
        intersectionList = CheckForIntersection(searchingDown.queue, searchingUp.queue)

        if len(intersectionList) > 0:
            intersectionNode = intersectionList[0]
            canvas.create_oval(intersectionNode.cordinates[0], intersectionNode.cordinates[1], intersectionNode.cordinates[2],
                       intersectionNode.cordinates[3], fill="blue")

            canvas.update()
            time.sleep(1)

            intersectionFound = True
            break


def CheckForIntersection(queue1, queue2):
    intersectionList = [value for value in queue1 if value in queue2]
    return intersectionList

def UCS():
    return None


