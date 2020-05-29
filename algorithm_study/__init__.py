# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : __init__.py.py
# __time__  : 2020/5/27 10:58 下午
from typing import List


class Solution:

    @classmethod
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans


if __name__ == '__main__':
    print(Solution.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
