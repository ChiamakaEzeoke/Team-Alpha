from tree import TreeNode

def serialise(array, coords):
    if not array:
        return None
    root = TreeNode(array[0]) if array[0] is not None else None
    coord = coords.pop(0)
    root.coords = coord
    array.pop(0)
    

    if root is None:
        return None
    
    queue = [root]


    while queue:
        current = queue.pop(0)
        if array:
            leftNode = TreeNode(array.pop(0)) if array else None
            if leftNode is None and array:
                array.pop(0)
            if leftNode:
                coord = coords.pop(0)
                leftNode.coords = coord
                current.left = leftNode
                queue.append(leftNode)
            
        if array:
            rightNode =  TreeNode(array.pop(0)) if array else None
            if rightNode is None and array:
                array.pop(0)
            if rightNode:
                coord = coords.pop(0)
                rightNode.coords = coord
                current.right = rightNode
                queue.append(rightNode)
    return root  


def bfs_console(root):
    if not root:
        return None
    result = []

    queue = []

    queue.append(root)

    level = 0

    levelLength = 0

    result = []

    while queue:
        result.append([])
        levelLength = len(queue)
        for i in range(levelLength):
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            result[level].append(current.val)
        level  +=1
    return result
        
def getHeight(node):
    if not node:
        return -1
    return 1 + max(getHeight(node.left), getHeight(node.right))