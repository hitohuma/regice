import bs4
from SuffixTree import SuffixTree
from Token import TokenStartTag, TokenAttr, TokenAttrVal, TokenString, TokenEndTag


class CodeSequences:
    def __init__(self, code):
        self.bs = bs4.BeautifulSoup(code, 'html.parser')
        self.tokens = self.tokenize(self.bs.body)
        self.start_tags, self.tokens_val = self.extract_tokens(self.tokens)
        self.st = SuffixTree(self.tokens_val)

    # 関数名考え直せ
    @staticmethod
    def extract_tokens(tokens):
        start_tags = []
        tokens_val = []
        for i, token in enumerate(tokens):
            tokens_val.append(token.value)
            if isinstance(token, TokenStartTag):
                start_tags.append(i)
        return start_tags, tokens_val

    def tokenize(self, bstag):
        tokens = list()
        tokens.append(TokenStartTag(bstag))
        for attr, vals in bstag.attrs.items():
            tokens.append(TokenAttr(attr))
            tokens.append(TokenAttrVal(vals))
        for elm in bstag.children:
            if isinstance(elm, bs4.element.Tag):
                tokens += self.tokenize(elm)
            elif isinstance(elm, bs4.element.NavigableString):
                tokens.append(TokenString(elm.string))
            else:
                raise Exception('!!!!otherClass')
        tokens.append(TokenEndTag())
        return tokens

    def __len__(self):
        return len(self.tokens)
