import sys


class DijkstraAlgorithm:
    def __init__(self,adjacency_matrix,start_vertex):
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(self.adjacency_matrix)
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.distances[start_vertex] = 0

    def get_min_vertex(self):
        min_vertex_value = sys.maxsize
        min_vertex_index = 0
        for index in range(self.v):
            if not self.visited[index] and self.distances[index] < min_vertex_value:
                min_vertex_value = self.distances[index]
                min_vertex_index = index
        return  min_vertex_index

    def calculate(self):
        for vertex in range(self.v):
            actual_vertex = self.get_min_vertex()
            print(f'cosidering vertex {actual_vertex}')
            self.visited[actual_vertex] = True

             # it has again the O(V) running time complexcity
            for other_vertex in range(self.v):
                # if there is connection between two nodes
                if self.adjacency_matrix[actual_vertex][other_vertex] > 0:
                    # is there a shorter path to the other vertex from actual vertex
                    if self.distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex]  < self.distances[other_vertex]:
                        self.distances[other_vertex] = self.distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex]
    def print_distances(self):
        print(self.distances)

