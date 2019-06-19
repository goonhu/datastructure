class Node():

    def __init__(self, data, left_node = None, right_node = None):

        self.data = data
        self.left_node = left.node
        self.right_node = right.node


class Binary_Search_Tree():

    def __init__(self):
        self.root = None
    def _insert(self, current_node, data):

        if data == current_node.data:
            raise Exception ("Duplicate values")

        elif data < current_node.data:
            if current_node.left_node is None:
                current_node.left_node = Node(data)
            else:
                self._insert(current_node.left_node, data)

        elif data > current_node.data:
            if current_node.right_node is None:
                current_node.right_node = Node(data)
            else:
                self._insert(current_node.right_node, data)

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)

        self._insert(data)

    def find(self, current_node, data):

        if value == current_node.data:
            return True

        elif value < current_node.data:
            if current_node.left_node is None:
                return False
            else:
                self.find(current_node.left_node, data)
        elif value > current_node.data:
            if current_node.right_node is None:
                return False
            else:
                self.find(current_node.right_node, data)


    def contains(self, data):

        if self.root is None:
            raise Exception ("Value not found")
        if self.root.data == data:
            return True
        return self.find(self.root, data)

        return self.find(self.root, data)


