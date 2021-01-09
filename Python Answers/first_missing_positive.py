import math
from typing import List

class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    #     if (  nums == None or len(nums) == 0  ) :
    #         return 1
    #     n = len(nums)
    #     containsOne = 0
    #     for i in range(n):
    #         if (nums[i] == 1):
    #             containsOne = 1
    #         elif (nums[i] < 0 or nums[i] > n):
    #             nums[i] = 1

    #     if containsOne == 0:
    #         return 1;

    #     for i in range(n):
    #         index = abs(nums[i]) - 1

    #         if (nums[index] > 0):
    #             nums[index] = -1 * nums[index]
        
    #     for i in range(n):
    #         if (nums[i] > 0):
    #             return i + 1
    #     return n + 1
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if num <= 0:
                nums[i] = 0

        for i,num in enumerate(nums):
            index = abs(num)-1
            if index >= 0 and index < len(nums):
                if nums[index] == 0:
                    nums[index] = -math.inf
                elif nums[index] > 0: # we dont want to make negative to be positive again, when its duplicated num
                    nums[index] *= -1

        for index,num in enumerate(nums):
            if num >= 0:
                return index + 1

        return len(nums) + 1


if __name__ == "__main__":
    s = Solution()

    print(s.firstMissingPositive([1,2,0]))


# https://leetcode.com/problems/first-missing-positive/discuss/872448/Python-O(n)-solution-with-constant-space-EXPLAINED-with-clear-train-of-thoughts