# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 990. 等式方程的可满足性.py
# __time__  : 2020/6/8 8:41 上午

import typing

"""
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或 "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 

 

示例 1：

输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
示例 2：

输出：["b==a","a==b"]
输入：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
示例 3：

输入：["a==b","b==c","a==c"]
输出：true
示例 4：

输入：["a==b","b!=c","c==a"]
输出：false
示例 5：

输入：["c==c","b==d","x!=z"]
输出：true
 

提示：

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] 和 equations[i][3] 是小写字母
equations[i][1] 要么是 '='，要么是 '!'
equations[i][2] 是 '='

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/satisfiability-of-equality-equations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        forestTree = list(range(26))
        def find(p):
            while forestTree[p] != p:
                p = forestTree[p]
            return p
        height = [1] * 26
        test = []
        for eq in equations:
            c1, c2 = ord(eq[0]) - ord('a'), ord(eq[-1]) - ord('a')
            if eq[1] == '=':
                r1 = find(c1)
                r2 = find(c2)
                if r1 == r2: continue
                # 测试数据量应该很小，路径压缩没什么提升
                if height[r1] < height[r2]:
                    forestTree[r1] = forestTree[r2]
                elif height[r2] < height[r1]:
                    forestTree[r2] = forestTree[r1]
                else:
                    forestTree[r2] = forestTree[r1]
                    height[r1] += 1
            else:
                test.append([c1, c2])
        for i, j in test:
            if find(i) == find(j): return False
        return True



