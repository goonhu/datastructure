class ArrayList():


    def __init__(self, initial_length = 2, resizing_factor = 2):

        self.main_list = [None] * initial_length
        self.resizing_factor = resizing_factor
        self.numOfelements= 0

    def expand_list(self):

        new_length = len(self.main_list) * 2
        changeOflength = new_length - len(self.main_list)
        self.main_list.extend([None]*changeOflength)

    def append(self, data):

        if self.numOfelements == len(self.main_list):
            self.expand_list()

        self.main_list[self.numOfelements] = data

        self.numOfelements += 1

    def extend(self, list_extension):

        for element in list_extension:
            self.append(element)

    def to_List(self):

        return self.main_list[:self.numOfelements]


    def __str__(self):

        return str(self.main_list)

    def __iter__(self):

        return iter(self.main_list)



if __name__ == "__main__":

    a = ArrayList()
    a.append(1)
    a.append(2)

    a.extend([3,4,5])

    print(a)
    for item in a:
        print(item)

    # a. to_List()
    # print(a)
    # for item in a:
    #     print(item)


