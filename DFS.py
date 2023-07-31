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
        actual_node.visited =True

        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visited = True
                stack.insert(n)






