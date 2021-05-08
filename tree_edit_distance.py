class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.parent = self
        self.id = None

    def __str__(self):
        return self.value + 'ff'


def make_tree(tree):
    root_node = make_node(tree)
    nodes = set_id(root_node[0])
    set_parent(root_node[0])
    print(root_node)


def set_id(tree):
    stack = [tree]
    nodes = []
    while stack:
        node = stack.pop()
        nodes.append(node)
        for child in node.children:
            stack.append(child)
    nodes.reverse()
    for i, node in enumerate(nodes):
        node.id = i
    return nodes


def set_parent(node):
    for child in node.children:
        child.parent = node
        set_parent(child)


def make_node(parent):
    if parent == ':end':
        return []
    return list(map(lambda x: Node(x[0], make_node(x[1])),
                    parent.items()))


tree1 = {
    'f': {
        'd': {
            'a': ':end',
            'c': {
                'b': ':end'
            }
        },
        'e': ':end'
    }
}
tree2 = {
    'f': {
        'c': {
            'd': {
                'a': ':end',
                'b': ':end'
            }
        },
        'e': ':end'
    }
}


if __name__ == "__main__":
    make_tree(tree2)
