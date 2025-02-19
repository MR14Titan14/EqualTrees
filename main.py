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
    return tree1, tree2


tree1, tree2 = read_from_file("input.txt")
