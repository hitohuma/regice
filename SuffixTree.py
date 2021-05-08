# トークン配列を利用したsuffix tree
class SuffixTree:
    ROOT = -1
    MAX_LEN = 0x7fffffff

    def __init__(self, tokens):
        self.tokens = tokens
        self.root = _Node(SuffixTree.ROOT, 0)
        for i in range(len(tokens)):
            parent, child, match, sub_match = self.longest_match(self.root, i)
            self.insert_node(parent, child, match, sub_match)
            # self.print_node(self.root, tokens)
            # print(i)

    def longest_match(self, node, node_start):
        tokens = self.tokens
        size = len(tokens)
        parent = node
        while node_start < size:
            child = node.search_child(tokens, size, tokens[node_start])
            if child is None: break
            child_len = child.len()
            sub_match = 1
            while sub_match < child_len:
                match = node_start + sub_match
                # 節の途中で不一致もしくはtokensの終端になった場合
                if match == size or tokens[match] != tokens[child.start + sub_match]:
                    return node, child, match, sub_match
            # node_start += child_len
            node_start += sub_match
            parent = node
            node = child
        # 過不足なく木のnodeとtokenの長さが一致した場合
        return parent, node, node_start, 0

    def search_pattern_sub(self, seq):
        seq_size = len(seq)
        tokens_size = len(self.tokens)
        node = self.root
        node_start = 0
        while node_start < seq_size:
            child = node.search_child(self.tokens, tokens_size, seq[node_start])
            if child is None: return None
            sub_match = 1
            k = child.len()
            while sub_match < k:
                match = node_start + sub_match
                if match == seq_size: return child
                # マッチしている部分で木の文字列の大きさに達しているか文字列の不一致が発生した場合
                if match == tokens_size or seq[match] != self.tokens[child.start + sub_match]:
                    return None
                sub_match += 1
            node_start += sub_match
            node = child
        return node

    def search_pattern(self, seq):
        node = self.search_pattern_sub(seq)
        return node is not None

    def search_pattern_all(self, seq):
        node = self.search_pattern_sub(seq)
        if node is None: return
        for x in node.traverse_leaf():
            yield x.start - x.depth

    @staticmethod
    def insert_node(parent, node, match, sub_match):
        # 過不足なく木のnodeとtokenの長さが一致したら葉だけを追加する
        if sub_match == 0:
            leaf = _Node(match, node.depth + node.len())
            node.insert_child(leaf)
        # nodeの途中で途切れる場合新しいnode+旧nodeという形に分割する
        else:
            new_node = _Node(node.start, node.depth)
            node.depth += sub_match
            node.start += sub_match
            parent.unlink_child(node)
            parent.insert_child(new_node)
            new_node.insert_child(node)
            leaf = _Node(match, node.depth)
            new_node.insert_child(leaf)

    # デバッグ用
    def print_node(self, node, tokens):
        if node.child is None:
            print('.' * node.depth + ','.join(tokens[node.start:]))
            # print(' ' * node.depth + tokens[node.start:])
        else:
            if node.start != SuffixTree.ROOT:
                print('*' * node.depth + ','.join(tokens[node.start:node.start + node.len()]))
                # print(' ' * node.depth + tokens[node.start:node.start + node.len()])
                # if node.len() == 0:
                #     print('stop')
                # print(node.start, node.start + node.len())
                # print(tokens[node.start:node.start + node.len()])
            x = node.child
            while x is not None:
                self.print_node(x, tokens)
                x = x.bros


class _Node:
    def __init__(self, start, depth):
        self.start = start
        self.depth = depth
        self.child = None
        self.bros = None

    # charから始まるchildがあるかを探す
    def search_child(self, tokens, size, token):
        child = self.child
        while child is not None:
            if child.start < size and tokens[child.start] == token:
                return child
            child = child.bros
        return None

    def insert_child(self, child):
        child.bros = self.child
        self.child = child

    def unlink_child(self, child):
        if self.child is child:
            self.child = child.bros
        else:
            # リンクを辿る
            node = self.child
            while node.bros is not None:
                # 弟が該当ノードの兄を見つけたら弟を飛ばして兄弟のリンクを貼り直す
                if node.bros is child:
                    node.bros = node.bros.bros
                    break
                node = node.bros

    # 節の長さを求める
    def len(self):
        if self.start == SuffixTree.ROOT: return 0
        if self.child is None: return SuffixTree.MAX_LEN  # 葉
        return self.child.depth - self.depth

    def traverse_leaf(self):
        if self.child is None:
            yield self
        else:
            node = self.child
            while node is not None:
                for x in node.traverse_leaf():
                    yield x
                # yield from node.traverse_leaf()
                node = node.bros


if __name__ == '__main__':
    tokens = ['body', '(string)', 'a', 'href', '(attr_val)', '(string)', '(tag_end)', '(string)', '(tag_end)', '(EOF)']
    # tokens = ['(b)', '(a)', '(n)', '(a)', '(n)', '(a)', '()', '(b)', '(a)', '(n)', '(a)', '(n)', '(a)', '($)']
    # tokens = []
    # tokens = 'banana banana$'
    # tokens = "aabbaaab$"
    st = SuffixTree(tokens)
    # print(st.search_pattern(['(b)', '(a)', '(n)', '(a)', '(n)', '(a)']))
    # print(st.search_pattern(['(a)', '(n)', '(a)']))
    print(st.search_pattern(['(a)', '(n)', '(a)']))
    # print([pattern for pattern in st.search_pattern_all(['(a)', '(n)', '(a)'])])
    st.print_node(st.root, tokens)
    # print(st.search_pattern('an'))
    # print([pattern for pattern in st.search_pattern_all('an')])
    pass
