class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def depth_first_search(start_node):
    stack = [start_node]
    start_node.visited = True

    while stack:
        actual_node = stack.pop()
        actual_node.visited = True
        print(actual_node.name)
        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                stack.append(n)

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

    depth_first_search(node2)




