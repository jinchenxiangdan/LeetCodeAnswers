from typing import List
'''
Author: Shawn Jin
Runtime: 52 ms, faster than 85.87% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
Memory Usage: 14.3 MB, less than 34.16% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]
