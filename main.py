from Tree import Tree
from equalize import make_equal

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk


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


def draw_graphs(tree1, tree2, deleted):
    G1 = nx.Graph()
    for node in tree1.nodes.values():
        if node.parent:
            G1.add_edge(node.parent.value, node.value)
    G2 = nx.Graph()
    for node in tree2.nodes.values():
        if node.parent:
            G2.add_edge(node.parent.value, node.value)

    fig = plt.figure(figsize=(10, 5))

    plt.subplot(121)
    pos1 = nx.spring_layout(G1)
    nx.draw(G1, pos1, with_labels=True, node_color='lightblue', node_size=500)
    plt.title("Tree1")
    plt.text(0.5, 0, deleted, color='red', fontsize='14', horizontalalignment='left', transform=plt.gca().transAxes)

    plt.subplot(122)
    pos2 = nx.spring_layout(G2)
    nx.draw(G2, pos2, with_labels=True, node_color='lightgreen', node_size=500)
    plt.title("Tree2")
    plt.text(0.5, 0, deleted, color='red', fontsize='14', horizontalalignment='left', transform=plt.gca().transAxes)

    return fig


def update(canvas, figures, current_page, diff):
    if 0 <= current_page[0]+diff < len(figures):
        current_page[0] += diff
        canvas.figure = figures[current_page[0]]
        canvas.draw()


def main():
    n, tree1, tree2 = read_from_file("input5.txt")

    orig = draw_graphs(tree1, tree2, "")
    operations, figures = make_equal(n, tree1, tree2, draw_graphs)

    print(f"Количество операций: {operations}")

    root = tk.Tk()
    root.title("Tree Visualizer")

    fig = plt.figure(figsize=(10, 5))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    figures.insert(0, orig)

    canvas.figure = figures[0]
    canvas.draw()
    current_page = [0]

    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.BOTTOM, pady=10, anchor=tk.CENTER)
    button = tk.Button(root, text="<", command=lambda: update(canvas, figures, current_page, -1))
    button.pack(side=tk.LEFT)
    button = tk.Button(root, text=">", command=lambda: update(canvas, figures, current_page, 1))
    button.pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    main()
