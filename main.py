import bs4

filepath = './sample/index.html'
f = open(filepath, 'r')
htmlcode = f.read()
f.close()
# Webページを取得して解析する

soup = bs4.BeautifulSoup(htmlcode, "html.parser")

# HTML全体を表示する
# print(soup.find('bostrinigdy'))
print(type(soup))
print(soup.body.children)
for elm in soup.body.children:
    print(type(elm))
    if isinstance(elm, bs4.element.Tag):
        # 自分のタグ名やクラス名をベクトルに足したあと子要素も
        print(elm.name)
        print(elm.attrs)
    elif isinstance(elm, bs4.element.NavigableString):
        # 値をベクトルに追加
        print([elm])
    else:
        print('!!!!otherClass')
