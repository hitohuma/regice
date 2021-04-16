from collections import defaultdict
from itertools import combinations
import bs4
import numpy as np


class Regice:
    def __init__(self):
        self.bows = []

    def analyze(self, filepath):
        f = open(filepath, 'r')
        htmlcode = f.read()
        f.close()
        # Webページを取得して解析する
        soup = bs4.BeautifulSoup(htmlcode, "html.parser")
        self.make_bow(soup.body)
        print(self.bows)
        print(len(self.bows))

    def all_similaries(self):
        for bow1, bow2 in combinations(self.bows, 2):
            similarity = self.calc_similarity(bow1, bow2)
            print(similarity)

    @staticmethod
    def calc_similarity(bow1, bow2):
        keys = set(bow1.keys()) | set(bow2.keys())
        # 普通にアクセスしてもdefaultdictだから0が返るがそれだとkeyが増えてしまう
        bow1_v = np.array([bow1.get(key, 0) for key in keys])
        bow2_v = np.array([bow2.get(key, 0) for key in keys])
        similarity = np.dot(bow1_v, bow2_v) / (np.linalg.norm(bow1_v) * np.linalg.norm(bow2_v))

        # デバッグ用
        if np.isnan(similarity):
            print(bow1_v)
        return similarity

    def make_bow(self, bstag):
        bow = defaultdict(lambda: 0)
        # 子要素が存在しないbstagがきたときに空集合を返してしまう
        # 自分の要素を取得できてないのでは？
        for elm in bstag.children:
            if isinstance(elm, bs4.element.Tag):
                # 自分のタグ名やクラス名をベクトルに足したあと子要素も
                bow[elm.name] += 1
                for attr, vals in elm.attrs.items():
                    bow[attr] += 1
                    if isinstance(vals, list):
                        for val in vals:
                            bow[val] += 1
                    else:
                        bow[vals] += 1
                bow = self.merge_defaultdict(bow, self.make_bow(elm))
            elif isinstance(elm, bs4.element.NavigableString):
                # 値をベクトルに追加
                bow[elm] += 1
            else:
                print('!!!!otherClass')

        #　デバッグ用
        if not bow:
            print(bow)
        self.bows.append(bow)
        return bow

    @staticmethod
    def merge_defaultdict(dict1, dict2):
        for key, value in dict2.items():
            dict1[key] += value
        return dict1
