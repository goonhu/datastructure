from Linked_List import LinkedList


class HashEntry():

    def __init__(self, key, value):

        self.key = key
        self.value = value

    def __str__(self):

        print_string = 'key: {} | value: {}'.format(
            str(self.key), str(self.value)
        )
        return print_string


class HashTable():

    def __init__(self, num_elements):

        self.num_elements = num_elements
        self.main_array = [LinkedList() for i in range(0, num_elements)]

    def hashing_key(self, key):

        hashed_key = hash(key)

        return hashed_key % len(self.main_array)

    def insert(self, key, value):

        data = HashEntry(key, value)

        index = self.hashing_key(key)

        self.main_array[index].append(data)

    def look_up_bucket(self, bucket, key):

        if bucket.head is None:
            raise KeyError('Key not found in the hash table')

        current_node = bucket.head

        if current_node.data.key == key:
            return current_node.data.value

        while current_node.next_node is not None:
            current_node = current_node.next_node
            if current_node.data.key == key:
                return current_node.data.value


        raise KeyError('Key not found in the hash table')


    def retrieve(self, key):

        item_index = self.hashing_key(key)
        bucket = self.main_array[item_index]

        return self.look_up_bucket(bucket, key)


if __name__ == '__main__':

    h = HashTable(10)
    h.insert(0, 'zero')
    h.insert(1, 'one')
    h.insert(2, 'two')
    h.insert(3, 'three')

    print(h.retrieve(2))
    print(h.retrieve(3))
