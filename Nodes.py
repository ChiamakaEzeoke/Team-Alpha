
class Nodes:
    def __init__(self, cordinates, left, right, value, head):
        self.cordinates = cordinates
        self.left = left
        self.right = right
        self.value = value
        self.head = head

    def __str__(self) -> str:
        return self.value

