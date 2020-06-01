# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 680. 验证回文字符串 Ⅱ.py
# __time__  : 2020/6/1 8:02 下午

from typing import List

"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # def checkPalindrome(low, high):
        #     i, j = low, high
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        # low, high = 0, len(s) - 1
        # while low < high:
        #     if s[low] == s[high]:
        #         low += 1
        #         high -= 1
        #     else:
        #         return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        # return True

        def checkIsPalind(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkIsPalind(low + 1, high) or checkIsPalind(low, high - 1)
        return True