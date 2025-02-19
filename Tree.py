from Node import Node


class Tree:
    def __init__(self):
        self.root = Node(1)
        self.nodes = {1: self.root}

    def add_node(self, parent_value, value):
        if parent_value in self.nodes:
            parent_node = self.nodes[parent_value]
            new_node = Node(value)
            parent_node.add_child(new_node)
            self.nodes[value] = new_node
        else:
            raise ValueError(f"Родителя {parent_value} ну существует")

    def get_structure(self):
        structure = {}
        for value, node in self.nodes.items():
            if node.parent:
                structure[value] = node.parent.value
        return structure

    def remove_node(self, value):
        if value not in self.nodes.keys() or value == 1:
            print(f"Невозможно удалить узел {value}.")
            return
        node_to_remove = self.nodes[value]
        parent_node = node_to_remove.parent
        parent_node.childs.remove(node_to_remove)
        for child in node_to_remove.childs:
            parent_node.add_child(child)
        del self.nodes[value]  # Remove from the node list
        print(f"Удалил узел {value}")
