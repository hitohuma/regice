from lib.html.parser import HTMLParser


class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs, startpos, endpos):
        print("Encountered a start tag:", tag, self.getpos())
        print(attrs)
        print(startpos, endpos, self.rawdata[startpos:endpos])

    def handle_endtag(self, tag, startpos, endpos):
        print("Encountered an end tag :", tag, self.getpos())
        print(startpos, endpos, self.rawdata[startpos:endpos])

    def handle_data(self, data, startpos, endpos):
        print("Encountered some data  :", data, self.getpos())
        print(startpos, endpos, self.rawdata[startpos:endpos])


if __name__ == '__main__':
    parser = MyParser()
    filepath2 = './sample/test.html'
    f2 = open(filepath2, 'r')
    code = f2.read()
    f2.close()
    # code = '<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>'
    parser.feed(code)