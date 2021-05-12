from Regice import Regice
from SuffixTree import SuffixTree
regice = Regice()
filepath = './sample/index.html'
# tokenizeしたものを木にして
tokens = regice.tokenize_from_file('./sample/index.html')
st = SuffixTree(tokens)
tokens2 = regice.tokenize_from_file('./sample/test.html')
print(tokens2)
num_token = len(tokens2)
res = []
for i in range(3, num_token):
    for j in range(num_token - i):
        res.append(tokens2[j:j+i])
        print(j, i)
        print([pattern for pattern in st.search_pattern_all(tokens2[j:j+i])])

# regice.analyze(filepath)
# regice.all_similaries()
