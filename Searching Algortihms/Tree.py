class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if currentNode.left == None:
                        currentNode.left = newNode
                        return
                    currentNode = currentNode.left
                else:
                    if currentNode.right == None:
                        currentNode.right = newNode
                        return
                    currentNode = currentNode.right

    def insert_many(self, nums):
        for i in nums:
            self.insert(i)

sample = tree()
sample.insert_many([9,4,6,20,170,15,1])