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


def IDFS(canvas, root, currentNode, nodeToFind, currentLevel):
    stopIteration = False
    maxLevel = 0
    colors = ["green", "deep pink", "yellow", "red"]
    while stopIteration is not True:
        color = colors[maxLevel]
        stopIteration = DLS(canvas, root, currentNode, nodeToFind, currentLevel, maxLevel, color)

        maxLevel = maxLevel + 1
