class minHeap():

    def __init__(self):

        self.main_array = []

    def get_left_child_index(self, parent_index):

        return (2*parent_index) + 1

    def get_right_child_index(self, parent_index):

        return (2*parent_index) + 2

    def get_parent_index(self, child_index):

        return int((child_index-1)/2)

    def does_have_left_child(self, parent_index):

        return self.get_left_child_index(parent_index) <= len(self.main_array)

    def does_have_right_child(self, parent_index):

        return self.get_right_child_index(parent_index) <= len(self.main_array)

    def does_have_parent(self, child_index):

        return self.get_parent_index(child_index) >= 0

    def get_left_child(self, parent_index):

        return self.main_array[self.get_left_child_index(parent_index)]

    def get_right_child(self, parent_index):

        return self.main_array[self.get_right_child_index(parent_index)]

    def get_parent(self, child_index):

        return self.main_array[self.get_parent_index(child_index)]

    def peek(self):

        if len(self.main_array) > 0:
            return self.main_array[0]
        else:
            raise Exception("HEAP is EMPTY")

    def swap(self, index1, index2):

        temp = self.main_array[index1]
        self.main_array[index1] = self.main_array[index2]
        self.main_array[index2] = temp

    def heapify_top_down(self):

        index = 0

        while self.does_have_left_child(index):

            smaller_child_index = self.get_left_child(index)

            if self.does_have_right_child(index) and self.get_right_child(index) < self.get_left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.main_array[index] < self.main_array[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
                index = smaller_child_index

    def heapify_down_top(self):

        last_index = len(self.main_array) - 1

        while self.does_have_parent(last_index):

            bigger_parent_index = self.get_parent_index(last_index)

            if self.get_parent(last_index) > self.main_array[last_index]:
                self.swap(last_index, bigger_parent_index)
                bigger_parent_index = last_index


    def pop(self):

        if len(self.main_array) > 0:

            elementTaken = self.main_array[0]
            self.main_array[0] = self.main_array[-1]
            self.main_array = self.main_array[:-1]
            self.heapify_top_down()

        return elementTaken

    def insert(self, value):

        self.main_array.append(value)
        self.heapify_down_top()



if __name__ == "__main__":

    heap = minHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(4)
    heap.insert(6)
    heap.insert(8)
    heap.insert(10)
    heap.insert(7)

    a = heap.pop()
    print(a)






