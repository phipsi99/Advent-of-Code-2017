from collections import Counter
from pathlib import Path
from matplotlib import pyplot as plt
import networkx as nx
import re

def do_main(debug_mode=False):
    with open(Path('07/input.txt')) as file:
        lines = [line.rstrip() for line in file]
    
    if debug_mode:
        with open(Path('07/test.txt')) as file:
            lines = [line.rstrip() for line in file]

    point_sum = 0
    graph = nx.DiGraph()
    weights = {}

    for line_index, line in enumerate(lines):
        #fwft (72) -> ktlj, cntj, xhth
        r = re.match(r"(\w+) \((\d+)\)(?: -> (.*))?", line)
        program, weight, childs_str = r.groups()
        weights[program] = int(weight)
        childs = []
        if childs_str:
            childs = childs_str.split(", ")
        graph.add_node(program)
        for child in childs:
            graph.add_edge(program, child)
    
    root = list(nx.topological_sort(graph))[0]
    print(root)
    
    def weight_rec(root: str, graph: nx.DiGraph):
        weight = weights[root]
        kid_weights = {}
        for kid in graph.successors(root):
            kid_weights[kid] = weight_rec(kid, graph)
        if len(set(kid_weights.values())) > 1:
            print(kid_weights)
            c = Counter(kid_weights.values())
            correct_weight = c.most_common(1)[0][0]
            for child, w in kid_weights.items():
                if w != correct_weight:
                    diff = correct_weight - w
                    print(f"{child} is wrong. It should be {weights[child] + diff}")
        for w in kid_weights.values():
            weight += w
        return weight
    
    print(weight_rec(root, graph))
    
    # nx.draw(graph, with_labels=True)
    # plt.show()

if __name__ == '__main__':
    do_main(False)