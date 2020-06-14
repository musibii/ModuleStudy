# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 1300. 转变数组后最接近目标值的数组和.py
# __time__  : 2020/6/14 6:03 下午
import bisect
import typing

"""
给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。

如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。

请注意，答案不一定是 arr 中的数字。

 

示例 1：

输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
示例 2：

输入：arr = [2,3,5], target = 10
输出：5
示例 3：

输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361
 

提示：

1 <= arr.length <= 10^4
1 <= arr[i], target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findBestValue(self, arr: typing.List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        r, ans, diff = max(arr), 0, target
        for i in range(1, r + 1):
            it = bisect.bisect_left(arr, i)
            cur = prefix[it] + (n - it) * i
            if abs(cur - target) < diff:
                ans, diff = i, abs(cur - target)
        return ans

    def findBestValue(self, arr: typing.List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        l, r, ans = 0, max(arr), -1
        while l <= r:
            mid = (l + r) // 2
            it = bisect.bisect_left(arr, mid)
            cur = prefix[it] + (n - it) * mid
            if cur <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        def check(x):
            return sum(x if num >= x else num for num in arr)

        choose_small = check(ans)
        choose_big = check(ans + 1)
        return ans if abs(choose_small - target) <= abs(choose_big - target) else ans + 1
