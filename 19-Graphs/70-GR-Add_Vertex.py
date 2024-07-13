class Graph:
    def __init__(self):
        self.adj_list = {}  # create a dictionary for key-value pairs of vertices and adjacent edges

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    # create key value pair with vertex as key
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():  # if the vertex is not already in the adjacency list
            self.adj_list[vertex] = []          #       add vertex with empty values. make empty list (the value of the vertex key) where we will store the edges adjacent to the vertex we are adding. for now, empty. we're just adding the vertex.
            return True
        return False




my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()



"""
    EXPECTED OUTPUT:
    ----------------
    A : []

"""