import time

start = time.time()

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, value):
        if self.key is None:
            self.key = value
        elif self.key < value:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def check_height(self, root):
        if not root:
            return 0
        else:
            lh_height = self.check_height(root.left)
            rh_height = self.check_height(root.right)

        return max(lh_height, rh_height) + 1

    def check_balance(self):
        lh_height = self.check_height(self.left)
        rh_height = self.check_height(self.right)

        if abs(lh_height - rh_height) > 1:
            return False

        left = self.left.check_balance() if self.left else True
        right = self.right.check_balance() if self.right else True

        return left and right


# Testing the code
node = Node(8)
node.insert(3)
node.insert(4)
node.insert(10)
node.insert(102)

print(node.check_balance())  # Output: False

end = time.end()
print(start - end) 
