class DirectedGraph:

    def __init__(self):
        #self.node = node
        self.graph = {}
        self.passed_nodes = []

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph:
            self.graph[node_a] = [node_b]
        else:
            self.graph[node_a].append(node_b)

    def get_neighbours_for(self, node):
        return(self.graph[node])

    def path_between(self, node_a, node_b):
        if node_a not in self.graph:
            return False
        self.passed_nodes.append(node_a)

        if node_b in self.graph[node_a]:
            self.passed_nodes = []
            return True

        for item in self.graph[node_a]:
            if item in self.graph and item not in self.passed_nodes:
                if self.path_between(item, node_b):
                    self.passed_nodes = []
                    return True
            self.passed_nodes.append(item)
        return False

    def __str__(self):
        graph_string = ""

        for item in self.graph:
            for element in self.graph[item]:
                graph_string += "({}, {})".format(item, element)
            graph_string += "\n"
        return graph_string
