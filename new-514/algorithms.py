import time
from queue import Queue
import collections
from heapq import heapify, heappush, heappop

def DFS(canvas, currentNode, valueToFind):
    if not currentNode:
        return
    if currentNode.val == valueToFind:
        canvas.create_oval(currentNode.coords[0], currentNode.coords[1], currentNode.coords[2],
                           currentNode.coords[3], fill="green")
        raise Exception("This was meant to happen, don't panic")
    canvas.create_oval(currentNode.coords[0], currentNode.coords[1], currentNode.coords[2],
                       currentNode.coords[3], fill="cyan")

    if currentNode.left is None and currentNode.right is None:
        return
    canvas.update()

    time.sleep(1)
    DFS(canvas, currentNode.left, valueToFind)

    canvas.update()

    time.sleep(1)
    DFS(canvas, currentNode.right, valueToFind)


def BFS(canvas, currentNode, valueToFind):
    queue = collections.deque([currentNode])

    while queue:
        current = queue.popleft()
        print(current.val)
        if current.val == valueToFind:
            canvas.create_oval(current.coords[0], current.coords[1], current.coords[2],
                               current.coords[3], fill="green")
            break

        canvas.create_oval(current.coords[0], current.coords[1], current.coords[2],
                           current.coords[3], fill="cyan")

        canvas.update()

        time.sleep(1)
        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


def DLS(canvas, currentNode, valueToFind, currentLevel=0, maxLevel=2, color="red"):
    if currentLevel > maxLevel:
        return
    if not currentNode:
        return

    if currentNode.val  == valueToFind:
        canvas.create_oval(currentNode.coords[0], currentNode.coords[1], currentNode.coords[2],
                           currentNode.coords[3], fill="green")
        raise Exception("Done searching")

    print("node - ", currentNode.val, "level - ", currentLevel)
    canvas.create_oval(currentNode.coords[0], currentNode.coords[1], currentNode.coords[2],
                       currentNode.coords[3], fill=color)

    if currentNode.left is None and currentNode.right is None:
        return

    canvas.update()

    time.sleep(1)
    DLS(canvas, currentNode.left, valueToFind, currentLevel + 1, maxLevel, color)

    canvas.update()

    time.sleep(1)

    DLS(canvas, currentNode.right, valueToFind, currentLevel + 1, maxLevel, color)


def IDFS(canvas, currentNode, valueToFind, currentLevel = 0):
    stop = False
    maximumLevel = 0
    colors = ["deep pink", "green",  "red", "yellow"]
    while not stop:
        color = colors[maximumLevel]
        stop = DLS(canvas, currentNode, valueToFind, currentLevel, maximumLevel, color)
        maximumLevel = maximumLevel + 1

# Uniform Cost Search Function
def UCS(canvas, currentNode, value):
    heap = []
    heapify(heap)
    heappush(heap, [currentNode, 0])
    while len(heap):
        highestNode = heap[0]
        heappop(heap)
        if highestNode[0].val == value:
            canvas.create_oval(highestNode[0].coords[0], highestNode[0].coords[1], highestNode[0].coords[2],
                               highestNode[0].coords[3], fill="red")
            print("found the node " + str(highestNode[0]) + " total cost " + str(highestNode[1]))
            break
        canvas.create_oval(highestNode[0].coords[0], highestNode[0].coords[1], highestNode[0].coords[2],
                               highestNode[0].coords[3], fill="red")
        print("explored node - " + str(highestNode[0])+ " total cost " + str(highestNode[1]))
        canvas.update()
        time.sleep(1)
        if highestNode[0].left:
            heappush(heap, [highestNode[0].left,  highestNode[1] + highestNode[0].leftPriority])
        if highestNode[0].right:
            print(heap)
            print(highestNode[1])
            heappush(heap, [highestNode[0].right , highestNode[1] + highestNode[0].rightPriority])


    return None


