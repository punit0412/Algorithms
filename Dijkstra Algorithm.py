import heapq


class Edges:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Node:
    def __init__(self,name):
        self.name = name
        # initially set to be false as node is not visited
        self.visited = False
        # adjacency list used for storing the children of a given node
        self.adjacency_list = []
        # to track the shortest path we must know the previous node of any node
        self.predecessor = None
        # this is the minimum distance from the source vertex
        self.min_distance = float('inf')
        # function used for comparing two object in python
        # as one object has several instance variables we have to define the logic which one we want to compare

    def __lt__(self, other_node):
        if __name__ == '__main__':
            return self.min_distance < other_node.min_distance


class DijkstraAlgorithm:
    def __init__(self):
        # we are using list as underlying data structure for heap
        # we are going to use binary heap instead of Fibonacci heap
        self.heap = []

    def calculate(self,start_vertex):
        # initialize the vertices
        start_vertex.min_distance = 0
        heapq.heappush(self.heap,start_vertex)
        # have to iterate until the heap is not empty

        while self.heap:
            # we pop the vertex with lowest min_distance parameter
            actual_vertex = heapq.heappop(self.heap)

            if actual_vertex.visited:
                continue

            # we have to consider the neighbours
            for edge in actual_vertex.adjacency_list:
                u = edge.start_vertex
                v = edge.target_vertex
                new_distance = u.min_distance + edge.weight

                # there is shortest path to vertex v
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    # update the heap - this is thr lazy implementation
                    # as it not update the previous value of a node instead of that it directly pushes
                    # so the runtime for finding the minimum node will be O(n) and O(logN) for heapify so total = O(N) + O(log(N)) = O(N)

                    heapq.heappush(self.heap,v)
            actual_vertex.visited = True

    @staticmethod
    def get_shortest_path(vertex):
        print(f"shortest path to the vertex is {vertex.min_distance}")
        actual_vertex = vertex
        while actual_vertex:
            print(f"{actual_vertex.name}")
            actual_vertex = actual_vertex.predecessor



if __name__ == '__main__':
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')
    node7 = Node('G')
    node8 = Node('H')

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node1.adjacency_list.append(node4)
    node2.adjacency_list.append(node5)
    node2.adjacency_list.append(node6)
    node3.adjacency_list.append(node4)
    node3.adjacency_list.append(node6)
    node4.adjacency_list.append(node7)
    node5.adjacency_list.append(node7)
    node6.adjacency_list.append(node7)

    edge1 = Edges(4,node1,node2)
    edge2 = Edges(3,node1,node3)
    edge3 = Edges(2,node1,node4)
    edge4 = Edges(7,node2,node5)
    edge5 = Edges(5,node3,node6)
    edge6 = Edges(4,node3,node4)
    edge7 = Edges(2,node2,node6)
    edge8 = Edges(6,node4,node7)
    edge9 = Edges(8,node5,node7)

    algo = DijkstraAlgorithm()
    algo.calculate(node1)
    algo.get_shortest_path(node7)