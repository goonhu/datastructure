# undirected graph : all the edges are bidirectional

class Node():

    def __init__(self, id, value):

        self.id = id
        self.value = value
        self.neighbour = [False]*10000

class Undirected_graph():

    def __init__(self):

        self.nodes = {}
        visited = []

    def check_duplicate_id(self, id):

        if id in self.nodes:
            raise Exception("This id is already in the graph")

    def insert(self, id, value):

        self.check_duplicate_id(id)

        self.nodes[id] = Node(id, value)

    def connect(self, id1, id2):

        self.nodes[id1].neighbour.append(id2)
        self.nodes[id2].neighbour.append(id1)

    def disconnect(self, id1, id2):

        self.nodes[id1].neighbour.remove(id2)
        self.nodes[id2].neighbour.remove(id1)

    def delete(self, id):


        for neighbourID in self.nodes[id].neighbour:
            self.nodes[neighbourID].neighbour.remove(id)

        self.nodes.pop(id, None)

    def has_DFS(self, visited, current_node_id, target_id):

        current_node = self.nodes[current_node_id]

        if visited[current_node_id]:
            return False

        if current_node_id == target_id:
            return True

        visited[current_node_id] = True

        for neighbour in current_node.neighbour:
            if self.has_DFS(visited, current_node_id, target_id):
                return True

        return False




if __name__ == "__main__":

    G = Undirected_graph()

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