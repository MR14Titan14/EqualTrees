from Tree import Tree


def read_from_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    n = int(lines[0])

    tree1 = Tree()
    tree2 = Tree()
    for line in lines[2:n + 1]:
        u, v = line.split(' ')
        tree1.add_node(int(u), int(v))
    for line in lines[n + 2:]:
        u, v = line.split(' ')
        tree2.add_node(int(u), int(v))
    return n, tree1, tree2


def get_conflict_nodes(tree1: Tree, tree2: Tree):
    conflict_nodes = []
    nodes = list(tree1.nodes.keys())
    nodes.remove(1)
    for i in nodes:
        if i not in tree1.nodes.keys() or i not in tree2.nodes.keys():
            conflict_nodes.append(i)
        else:
            if tree1.nodes[i].parent.value is not tree2.nodes[i].parent.value:
                conflict_nodes.append(i)
    return conflict_nodes


def make_equal(n, tree1: Tree, tree2: Tree):
    operations = 0
    conflict_nodes = get_conflict_nodes(tree1, tree2)
    while conflict_nodes != []:
        conflict_parents = {i: 0 for i in range(1, n + 1)}
        for i in conflict_nodes:
            conflict_parents[tree1.nodes[i].parent.value] += 1
            conflict_parents[tree2.nodes[i].parent.value] += 1
        if 1 in conflict_parents.keys():
            del conflict_parents[1]
        worst_node, conf_num = max(conflict_parents.items(), key=lambda item: item[1])
        if conf_num == 1:
            temp = [node for node in conflict_nodes if tree1.nodes[node].parent.value == worst_node]
            worst_node = temp[0]
        tree1.remove_node(worst_node)
        tree2.remove_node(worst_node)
        print(f"Удалил узел {worst_node} в дереве 1")
        print(f"Удалил узел {worst_node} в дереве 2")
        operations += 2
        conflict_nodes = get_conflict_nodes(tree1, tree2)
    return operations


n, tree1, tree2 = read_from_file("input3.txt")

print(make_equal(n, tree1, tree2))
