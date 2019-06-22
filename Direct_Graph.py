


class Node():

    def __init__(self, id, value):

        self.id = id
        self.value = value
        self.neighbour = []



class Graph():

    def __init__(self):

        self.nodes = {}

    def check_duplicate_id(self, id):#

        if id in self.nodes:
            raise Exception("Already same id in the dictionary of nodes representing Graph")

    def insert(self, id, value):

        self.check_duplicate_id(id)

        self.nodes[id] = Node(id, value)

    def connect(self, id1, id2):

        self.nodes[id1].neighbour.append(id2)

    def disconnect(self, id1, id2):

        self.nodes[id1].neighbour.remove(id2)

    def delete(self, id):
    #   delete node off the graph

        for i in range(len(self.nodes[id].neighbour)):
            self.nodes[id].neighbour.remove(i)


        self.nodes.pop(id, None)

    def __str__(self):

        node_list = []

        for node_id, node in self.nodes.items():

            node_str = 'Id: {}, Value: {}, Neighbour Ids: {}'.format(
                node.id, str(node.value), [str(i) for i in node.neighbour]
            )

            node_list.append(node_str)

        return ' '.join(node_list)




if __name__=="__main__":

    G = Graph()

    G.insert('A', 1)
    G.insert('B', 2)
    G.insert('C', 2)
    G.insert('D', 2)
    G.insert('E', 2)

    print(G, '\n')

    G.connect('A', 'B')
    G.connect('A', 'C')
    G.connect('D', 'E')
    G.connect('C', 'D')
    G.connect('A', 'D')

    print(G, '\n')

    G.disconnect('A', 'D')

    print(G, '\n')

    G.delete('B')
