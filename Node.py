class Node:
    def __init__(self, value):
        self.value = value
        self.childs = []
        self.parent = None

    def add_child(self, child_node):
        child_node.parent = self
        self.childs.append(child_node)
