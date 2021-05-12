import bs4
import unittest
from Token import TokenStartTag, TokenAttr, TokenAttrVal, TokenString, TokenEndTag


class TestToken(unittest.TestCase):
    # TokenStartTag以外の初期化確認
    def test_token_init(self):
        token_attr = TokenAttr('href')
        self.assertEqual(token_attr.value, '(Attr):href')

        token_attr_val = TokenAttrVal('https://foobar.com')
        self.assertEqual(token_attr_val.value, '(AttrVal)')
        self.assertEqual(token_attr_val.raw_value, 'https://foobar.com')

        token_string = TokenString('hello')
        self.assertEqual(token_string.value, '(String)')
        self.assertEqual(token_string.raw_value, 'hello')

        token_end_tag = TokenString('hello')
        self.assertEqual(token_end_tag.value, '(String)')
        self.assertEqual(token_end_tag.raw_value, 'hello')

    def test_token_starttag_init(self):
        code = '<p>hello</p>'
        bs = bs4.BeautifulSoup(code, "html.parser")
        token_start_tag = TokenStartTag(bs.p)
        self.assertEqual(token_start_tag.value, '(StartTag):p')


if __name__ == '__main__':
    unittest.main()
