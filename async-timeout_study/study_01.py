# -*- coding: utf-8 -*-
# __file__  : study_01.py
# __time__  : 2020/8/6 10:32 AM
from typing import List

from async_timeout import timeout

async with timeout:
    ''


class Solution:
    def num_sum(self, nums: List[int], k: int) -> List[int]:
        mirror = {}
        for n in nums:
            if n in mirror:
                return []
