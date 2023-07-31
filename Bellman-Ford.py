class Edges:
    def __init__(self,start_vertex,weight,target_vertex):
        self.start_vertex = start_vertex
        self.weight = weight
        self.target_vertex = target_vertex

class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.predecessor = None
        self.min_distance = float('inf')


class BellmanFordAlgorithm:
    def __init__(self,vertex_list,edge_list,start_vertex):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.start_vertex = start_vertex
        self.has_cycle = False

    def find_shortest_path(self):
        self.start_vertex.min_distance = 0
        # iterate through V-1 vertices
        # Final running time is O(V*E)
        for _ in range(len(self.vertex_list)-1):
            # in every iteration we have to consider all the edges
            for edge in self.edge_list:
                # we have to calculate whether there is shorter path
                u = edge.start_vertex
                v = edge.target_vertex
                dist = u.min_distance + edge.weight

                if dist < v.min_distance:
                    v.min_distance = dist
                    v.predecessor = u
        # After V-1 iteration we have to check for negative cycle
        for edge in self.edge_list:
            if self.check_cycle(edge):
                print("Negative cycle detected...")
                return

    def check_cycle(self,edge):
        # If the total cost(min_distance) of a given vertex decreases after V-1 iteration
        # it means there is negative cycle
        if edge.start_vertex.min_distance + edge.weight < edge.target_vertex.min_distance:
            self.has_cycle = True
            return True
        else:
            return False

    def get_shortest_path(self,vertex):
        if not self.has_cycle:
            print(f"Shortest Path exist with value {vertex.min_distance}")
            node = vertex
            while node:
                print(node.name)
                node = node.predecessor
        else:
            print("There is a negative cycle in G(V,E)...")


if __name__ == "__main__":
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')
    node7 = Node('G')
    edge1 = Edges(node1,5,node2)
    edge2 = Edges(node1,9,node5)
    edge3 = Edges(node2,5,node5)
    edge4 = Edges(node2,12,node3)
    edge5 = Edges(node2,7,node4)
    edge6 = Edges(node3,3,node4)
    edge7 = Edges(node3,1,node6)
    edge8 = Edges(node4,9,node7)
    edge9 = Edges(node5,6,node3)
    edge10 = Edges(node5,4,node6)
    edge11 = Edges(node6,2,node7)
    edge12 = Edges(node7,6,node3)

    node1.adjacency_list.append(edge1)
    node1.adjacency_list.append(edge2)
    node2.adjacency_list.append(edge3)
    node2.adjacency_list.append(edge4)
    node2.adjacency_list.append(edge5)
    node3.adjacency_list.append(edge6)
    node3.adjacency_list.append(edge7)
    node4.adjacency_list.append(edge8)
    node5.adjacency_list.append(edge9)
    node5.adjacency_list.append(edge10)
    node6.adjacency_list.append(edge11)
    node7.adjacency_list.append(edge12)

    vertices = [node1,node2,node3,node4,node5,node6,node7]
    edges = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12)

    algorithm = BellmanFordAlgorithm(vertex_list=vertices,edge_list=edges,start_vertex=node1)
    algorithm.get_shortest_path(node7)

















