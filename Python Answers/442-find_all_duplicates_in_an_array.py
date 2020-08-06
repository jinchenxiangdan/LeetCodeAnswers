class Solution:
    '''
    Using sort before checking
    The run time should be O(nlog(n))
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                out.append(nums[i])
        return out


    '''
    Using input array itself as a hash to store which numbers have been seen before
    The run time should be O(n)
    '''
    # def findDuplicates(self, nums: List[int]) -> List[int]:
        
    #     out = []
    #     for num in nums:
    #         if nums[abs(num)-1] < 0:
    #             res.append(abs(num))
    #         else:
    #             nums[abs(num)-1] *= -1
    #     return out
