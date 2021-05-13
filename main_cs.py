from CodeSequences import CodeSequences
filepath1 = './sample/index.html'
f1 = open(filepath1, 'r')
code1 = f1.read()
f1.close()
cs1 = CodeSequences(code1)

filepath2 = './sample/test.html'
f2 = open(filepath2, 'r')
code2 = f2.read()
f2.close()
cs2 = CodeSequences(code2)

for idx in cs2.start_tags:
    for num_token in range(3, len(cs2) - idx):
        tokens = cs2.tokens_val[idx:idx+num_token+1]
        match_idxes = cs1.st.search_pattern_all(tokens)
        print('match_idxes')
        print(match_idxes)
        if match_idxes is not None:
            for match in match_idxes:
                print(cs1.tokens_val[match:match+num_token+1])
