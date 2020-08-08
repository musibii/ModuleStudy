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


"""
def nums_sum(nums: List[int], k: int) -> List[Union[List[int], int]]:
    sorted_nums = sorted((num for num in nums if num <= k))
    if not sorted_nums:
        return [min(nums)]
    if sum(sorted_nums) <= k:
        return sorted_nums
    
    def nums_nums(nums: List[int], k: int, i, j):
        if i > j:
            return [[False]]
        if nums[i] > k:
            return [[False]]
        if nums[i] == k:
            return [[k]]
        result = []
        for m in range(i, j - 1):
            if nums[m] == k:
                result.append([k])
            tem = nums_nums(nums, k - nums[m], m + 1, j)
            for xx in tem:
                if xx:
                    xx.insert(0, nums[m])
                    result.append(xx)
        return result

    result = nums_nums(sorted_nums, k, 0, len(sorted_nums))
    result = [i for i in result if False not in i]
    if not result:
        min_num, max_num = sorted_nums[0], sum(sorted_nums)
        while min_num <= k <= max_num:
            k -= 1
            result = nums_nums(sorted_nums, k, 0, len(sorted_nums))
            if result:
                return [i for i in result if False not in i]
    else:
        return result
"""


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    k = 100
    print('nums: %s, k: %s' % (nums, k))
    print('*' * 50)
    print('result')
    print(Solution().nums_sum(nums, k))
