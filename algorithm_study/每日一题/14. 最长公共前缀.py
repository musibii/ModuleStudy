# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 14. 最长公共前缀.py
# __time__  : 2020/6/15 1:29 下午

import typing
from optparse import OptionParser

"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestCommonPrefix(self, strs: typing.List[str]) -> str:
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

    def longestCommonPrefix1(self, strs):
        ans = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                ans += i[0]
            else:
                break
        return ans


# ["flower","flow","flight"]
# ["dog","racecar","car"]
Solution().longestCommonPrefix1(["flower", "flow", "flight"])


def enumerate(collection):
    'Generates an indexed series:  (0,coll[0]), (1,coll[1]) ...'
    i = 0
    it = iter(collection)
    while 1:
        yield (i, it.next())
        i += 1
OptionParser