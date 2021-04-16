import unittest
from Regice import Regice
from collections import defaultdict
import math


class TestRegice(unittest.TestCase):
    def test_calc_similarity(self):
        regice = Regice()
        bow1 = [('div', 4), ('p', 2), ('input', 3), ('form', 4)]
        dbow1 = defaultdict(int)
        for k, v in bow1:
            dbow1[k] = v
        bow2 = [('div', 6), ('p', 1), ('span', 3)]
        dbow2 = defaultdict(int)
        for k, v in bow2:
            dbow2[k] = v
        result = regice.calc_similarity(dbow1, dbow2)
        ans = 26 / math.sqrt(45 * 46)  # cos類似度
        self.assertTrue(math.isclose(result, ans))


if __name__ == '__main__':
    unittest.main()
