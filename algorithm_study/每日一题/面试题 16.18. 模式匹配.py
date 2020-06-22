# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 面试题 16.18. 模式匹配.py
# __time__  : 2020/6/22 11:08 下午

import typing

"""
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：

输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：

输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：

输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：

0 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pattern-matching-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # def patternMatching(self, pattern: str, value: str) -> bool:
    #     # 边界情况处理
    #     if not pattern: return not value
    #     if len(pattern) == 1: return True

    #     # 构造正则表达式：重点是正则表达式的“后向引用”
    #     rega, regb = ('\\1', '\\2') if pattern[0] == 'a' else ('\\2', '\\1')
    #     p = pattern.replace('a', '(\\w*)', 1).replace('b', '(\\w*)', 1).replace('a', rega).replace('b', regb)
    #     p = '^' + p + '$'
    #     m = re.match(p, value)

    #     # 匹配到 && (模式长度为1 || 模式长度为2 && 两个模式不相同)
    #     return bool(m and (len(m.groups()) == 1 or m.groups()[0] != m.groups()[1]))

    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == "a")
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = "".join("a" if ch == "b" else "b" for ch in pattern)

        if not value:
            return count_b == 0
        if not pattern:
            return False

        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == "a":
                        sub = value[pos : pos + len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos : pos + len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True

        return False
