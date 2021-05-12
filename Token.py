class Token:
    def __init__(self, value):
        self.value = value


class TokenStartTag(Token):
    PREFIX = '(StartTag):'

    def __init__(self, bstag):
        super().__init__(TokenStartTag.PREFIX + bstag.name)
        self.bstag = bstag


class TokenAttr(Token):
    PREFIX = '(Attr):'

    def __init__(self, value):
        super().__init__(TokenAttr.PREFIX + value)


class TokenAttrVal(Token):
    VALUE = '(AttrVal)'

    def __init__(self, raw_value):
        super().__init__(TokenAttrVal.VALUE)
        self.raw_value = raw_value


class TokenString(Token):
    VALUE = '(String)'

    def __init__(self, raw_value):
        super().__init__(TokenString.VALUE)
        self.raw_value = raw_value


class TokenEndTag(Token):
    VALUE = '(EndTag)'

    def __init__(self):
        super().__init__(TokenEndTag.VALUE)
