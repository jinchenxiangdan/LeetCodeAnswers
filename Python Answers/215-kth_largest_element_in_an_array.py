class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Author: Shawn Jin
        Runtime: 56 ms, faster than 96.36% of Python3 online submissions for Kth Largest Element in an Array.
        Memory Usage: 15 MB, less than 75.24% of Python3 online submissions for Kth Largest Element in an Array.
        """
        nums.sort(reverse=True)
        return nums[k]