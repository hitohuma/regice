import bs4
import unittest
from Token import TokenStartTag, TokenAttr, TokenAttrVal, TokenString, TokenEndTag
from CodeSequences import CodeSequences


class TestCodeSequences(unittest.TestCase):
    def test_code_sequences_init(self):
        code = """
            <body>
                <a href="https://aaaaaa.com">home</a>
            </body>
        """
        code_sequences = CodeSequences(code)
        self.assertEqual(code_sequences.start_tags, [0, 2])
        expected = ['(StartTag):body', '(String)', '(StartTag):a', '(Attr):href', '(AttrVal)', '(String)', '(EndTag)', '(String)', '(EndTag)']
        self.assertEqual(code_sequences.tokens_val, expected)
        self.assertEqual(len(code_sequences), len(expected))
        self.assertEqual(code_sequences.st.search_pattern_all(['(StartTag):a']), [2])
        self.assertEqual(code_sequences.st.search_pattern_all(['(String)']), [1, 5, 7])
        self.assertEqual(code_sequences.st.search_pattern_all(['(StartTag):a', '(Attr):href', '(AttrVal)', '(String)', '(EndTag)']), [2])


if __name__ == '__main__':
    unittest.main()
