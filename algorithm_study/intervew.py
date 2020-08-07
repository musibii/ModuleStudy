# -*- coding: utf-8 -*-
# __file__  : intervew.py
# __time__  : 2020/8/6 7:39 PM

"""
1、【编程题】给一个不重复的整数数组A，同时给一个定值K，找出A中所有能组成和为K的所有组合，若没有则给出最接近的数的集合
例：
输入：[1,2,3,4,5,6], 6
解释：定值6可组成，直接输出和为6的数的集合
输出：[1,2,3],[2,4],[1,5],[6]
输入：[1,2,3,4,5], 100
解释：定值100无法组成，输出所有最接近的组合
输出：[1,2,3,4,5]



要求：把要求的测试用例跑通，并附上截图
"""
from typing import List


class Solution:
    def nums_sum(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        nums = sorted(nums)
        list_length = len(nums)
        res = []

        def inner(i, tmp, target):
            if target == 0:
                res.append(tmp)
                return
            if i == list_length or target < nums[i]:
                return
            for j in range(i, list_length):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                inner(j + 1, tmp + [nums[j]], target - nums[j])

        inner(0, [], k)

        if not res:
            # 表示没有符合条件的，则输出最接近目标的集合
            numsum = sum(nums)
            if numsum < k:
                return nums
        return res


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 100
    print('nums: %s, k: %s' % (nums, k))
    print('*' * 50)
    print('result')
    print(Solution().nums_sum(nums, k))
