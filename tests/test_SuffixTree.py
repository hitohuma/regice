from pprint import pprint, pp
import unittest
from SuffixTree import SuffixTree


class TestSuffixTree(unittest.TestCase):
    def test_init_suffix_tree(self):
        tokens = ['body', '(string)', 'a', 'href', '(attr_val)', '(string)', '(tag_end)', '(string)', '(tag_end)', '(EOF)']
        st = SuffixTree(tokens)
        self.assertTrue(st.search_pattern(['a', 'href', '(attr_val)']))
        self.assertFalse(st.search_pattern(['p', 'class', '(attr_val)']))
        # self.print_node(st.root, tokens)

    def test_tree_array(self):
        tokens = 'aabbaaab$'
        st = SuffixTree(tokens)
        # pprint(st.tree_array(), sort_dicts=False, width=10)
        # pp(st.tree_array(), sort_dicts=False, width=10)



if __name__ == '__main__':
    unittest.main()
