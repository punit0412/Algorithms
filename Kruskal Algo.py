class Vertex:
    def __init__(self,name):
        self.name = name
        self.node = None


class Edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight = weight
        self.target_vertex = target_vertex
        self.start_vertex = start_vertex

    def __lt__(self, other_node):
        return self.weight < other_node.weight


class Node:
    def __init__(self,rank,node_id,parent = None):
        self.rank = rank
        self.node_id = node_id
        self.parent = parent


class DisjointSet:
    def __init__(self,vertex_list):
        self.vertex_list = vertex_list
        self.root_nodes = []
        self.make_sets()

    def find(self,node):
        current_node = node

        while current_node.parent:
            current_node = current_node.parent

        root = current_node
        current_node = node

        while current_node is not root:
            temp = current_node.parent
            current_node.parent = root
            current_node = temp

        return root.node_id

    def merge(self,node1,node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:return

        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]

        if root1.rank < root2.rank:
            root2.parent = root1
        elif root1.rank > root2.rank:
            root1.parent = root2
        else:
            root1.parent = root2
            root1.rank += 1

    def make_sets(self):
        for v in self.vertex_list:
            node = Node(0,len(self.root_nodes))
            v.node = node
            self.root_nodes.append(node)

class KruskalAlgorithm:
    def __init__(self,vertex_list,edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list

    def mst(self):
        disjoint_set = DisjointSet(self.vertex_list)
        mst = []

        self.edge_list.sort()

        for edge in self.edge_list:
            u = edge.start_vertex
            v = edge.target_vertex

            if disjoint_set.find(u.node) != disjoint_set.find(v.node):
                mst.append(edge)
                disjoint_set.merge(u.node, v.node)

        for edge in mst:
            print(f'{edge.start_vertex.name} - {edge.target_vertex.name} - {edge.weight}')


if __name__ == '__main__':
    vertex1 = Vertex('A')
    vertex2 = Vertex('B')
    vertex3 = Vertex('C')
    vertex4 = Vertex('D')
    vertex5 = Vertex('E')
    vertex6 = Vertex('F')
    vertex7 = Vertex('G')


    edge1 = Edge(2,vertex1,vertex2)
    edge2 = Edge(5,vertex1,vertex5)
    edge3 = Edge(6,vertex1,vertex3)
    edge4 = Edge(1,vertex1,vertex6)
    edge5 = Edge(3,vertex2,vertex5)
    edge6 = Edge(3,vertex2,vertex4)
    edge7 = Edge(1,vertex3,vertex4)
    edge8 = Edge(2,vertex6,vertex3)
    edge9= Edge(5,vertex6,vertex7)
    edge10 = Edge(5,vertex7,vertex4)

    vertex_list = [vertex1,vertex2,vertex3,vertex4,vertex5,vertex6,vertex7]
    edge_list = [edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10]

    algorithm = KruskalAlgorithm(vertex_list,edge_list)
    algorithm.mst()

