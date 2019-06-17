class Node():

    def __init__(self, data, next_node = None):

        self.data = data
        self.next_node = next_node



class LinkedList():

    def __init__(self, input_arr = []):

        self.head = None
        self._fill_from_array(input_arr)

    def _fill_from_array(self, input_arr):

        for item in input_arr[::-1]:
            self.prepend(item)

    def append(self, data):

        if self.head is None:
            self.head = Node(data)


        current_node = self.head

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = Node(data)

    def prepend(self, data):

        new_head = Node(data, next_node = self.head)

        self.head = new_head

    def delete_first_node_with_value(self, data):

        if self.head is None:
            return

        current_node = self.head

        while current_node.next_node is not None:

            if current_node.next_node.data == data:
                current_node.next_node = current_node.next_node.next_node
                return

            current_node = current_node.next_node

    def size(self):
        a = 0
        current_node = self.head
        while current_node.next_node is not None:
            a += 1
            current_node = current_node.next_node

        print(a)

if __name__ == '__main__':

    L = LinkedList()
    print('\n Initial Linkedlist')

    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    print('\n Elements have been appended to the linkedlist')

    L.prepend(5)
    L.prepend(6)
    print('\n Elements have been prepended to the linkedlist')

    L.delete_first_node_with_value(2)
    print('\n linkedlist with 2 deleted and the size of linkedlist has been reduced by 1 \n')

    L.size()
