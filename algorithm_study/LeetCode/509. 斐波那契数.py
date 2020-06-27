# -*- coding: utf-8 -*-
# __file__  : 509. 斐波那契数.py
# __time__  : 2020/6/27 10:04 下午

import typing


"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.

输入：5
输出：
解释：F(5) = F(4) + F(3) = 3 + 2 = 5
 

提示：

0 ≤ N ≤ 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # def fib(self, N: int) -> int:
    #     if N <= 1:
    #         return N
    #     return self.memoize(N)
    #
    # def memoize(self, N: int) -> {}:
    #     cache = {0: 0, 1: 1}
    #
    #     # Since range is exclusive and we want to include N, we need to put N+1.
    #     for i in range(2, N + 1):
    #         cache[i] = cache[i - 1] + cache[i - 2]
    #
    #     return cache[N]
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        if N == 2:
            return 1

        current = 0
        pre1 = 1
        pre2 = 1
        for i in range(3, N + 1):
            current = pre1 + pre2
            pre2 = pre1
            pre1 = current
        return current

    # 备忘录，DPtable


if __name__ == "__main__":

    print(Solution().fib(300))
