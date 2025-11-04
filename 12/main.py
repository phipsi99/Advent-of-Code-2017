from pathlib import Path

import networkx as nx

def do_main(debug_mode=False):
    with open(Path('12/input.txt')) as file:
        lines = [line.rstrip() for line in file]

    if debug_mode:
        with open(Path('12/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0

    graph = nx.Graph()

    for line_index, line in enumerate(lines):
        root = int(line.split(" <-> ")[0])
        childs = [int(i) for i in line.split(" <-> ")[1].split(", ")]
        if not graph.has_node(root):
            graph.add_node(root)
        for child in childs:
            graph.add_edge(root, child)

    reachable = nx.node_connected_component(graph, 0)
    print(len(reachable))

    group_count = 0
    while len(graph.nodes) > 0:
        reachable = list(nx.node_connected_component(graph, list(graph.nodes)[0]))
        group_count += 1
        for node in reachable:
            graph.remove_node(node)
    print(group_count)


if __name__ == '__main__':
    do_main(False)