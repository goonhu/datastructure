from Linked_List import LinkedList


class Stack(LinkedList):

    def delete_head(self):

        self.head = self.head.next_node

    def pop(self):

        if self.head is None:
            raise Exception("Stack is empty")

        data = self.head.data
        self.delete_head()

        return data

    def push(self, data):

        # push -> adding data on the head of Linked List

        self.prepend(data)

    def peek(self):

        if self.head is None:
            raise Exception("Stack is empty")

        return self.head.data

    def __str__(self):

        if self.head is None:
            raise Exception("Stack is empty")



if __name__ == "__main__":

    s = Stack()

    s.push(0)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)


    print('peek: ', s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    
