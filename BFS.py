class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def breadth_first_search(start_node):
    queue = [start_node]
    start_node.visited = True  # set the visited node to be true so further it can not be visited

    while queue:
        actual_node = queue.pop(0)  # FIFO
        actual_node.visited = True
        print(actual_node.name)
        # insert the unvisited neighbors of node
        for n in actual_node.adjacency_list:
            if not n.visited:
                queue.append(n)


if __name__ == '__main__':
    node1 = Node('d')
    node2 = Node('e')
    node3 = Node('g')
    node4 = Node('f')
    node5 = Node('r')
    node6 = Node('s')

    node1.adjacency_list.append(node2)
    node1.adjacency_list.append(node3)
    node2.adjacency_list.append(node5)
    node2.adjacency_list.append(node6)
    node3.adjacency_list.append(node5)
    node5.adjacency_list.append(node4)

    breadth_first_search(node2)



