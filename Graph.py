class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = dict()

    def add_vertex(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connections(self):
        for key in self.adjacent_list:
            connections = ''
            for node in self.adjacent_list[key]:
                connections += f'{node}, '
            print(f"{key} --> {connections.rstrip(' ,')}")
