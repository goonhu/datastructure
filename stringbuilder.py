class StringBuilder():


    def __init__(self):

        self.string_list = []

    def append(self, *args):

        for string in args:
            self.string_list.append(string)

    def to_String(self):

        return ''.join(self.string_list)

    def extend(self, list):

        return self.string_list.extend(list)

    def __add__(self, other):

        if type(other) != list:
            list = [list]

        current_string_list = self.string_list.copy()
        temp_list = StringBuilder()
        temp_list.extend(current_string_list)

        temp_list.extend(other)

        return temp_list

if __name__ == '__main__':

    s = StringBuilder()

    s.append('Hello', ' ', 'world')
    s.extend(['.', ' ', 'aaa'])

    print(s.to_String())

