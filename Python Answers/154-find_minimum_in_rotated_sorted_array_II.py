from typing import List
'''
Author: Shawn Jin
Runtime: 48 ms, faster than 95.32% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
Memory Usage: 14.2 MB, less than 82.75% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]
