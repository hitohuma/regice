import unittest
from SuffixTree import SuffixTree


class TestSuffixTree(unittest.TestCase):
    def test_init_suffix_tree(self):
        tokens = ['body', '(string)', 'a', 'href', '(attr_val)', '(string)', '(tag_end)', '(string)', '(tag_end)', '(EOF)', '(RJI)']
        st = SuffixTree(tokens)
        # self.print_node(st.root, tokens)

    def print_node(self, node, tokens):
        if node.child is None:
            print('  ' * node.depth + ','.join(tokens[node.start:]))
        else:
            if node.start != SuffixTree.ROOT:
                print('  ' * node.depth + ','.join(tokens[node.start:node.start + node.len()]))
            x = node.child
            while x is not None:
                self.print_node(x, tokens)
                x = x.bros


if __name__ == '__main__':
    unittest.main()
