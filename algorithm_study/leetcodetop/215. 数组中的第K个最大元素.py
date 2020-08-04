# -*- coding: utf-8 -*-
# __file__  : 215. 数组中的第K个最大元素.py
# __time__  : 2020/8/4 10:25 AM

"""
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import heapq
from typing import List


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for c in nums:
            heapq.heappush(q, c)
            while len(q) > k:
                heapq.heappop(q)
        return heapq.heappop(q)

# def func(nums, k):
#     q = []
#     for c in nums:
#         heapq.heappush(q, c)
#         while len(q) > k:
#             heapq.heappop(q)
#     return heapq.heappop(q)

if __name__ == '__main__':
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
