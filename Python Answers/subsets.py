class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # sort first 
        nums.sort()
        out = []
        backtrack(nums, out, [], 0)
        return out

        def backtrack(nums: List[int], out: List[List[int]], curr: List[int], start: int):
            # basecase: in this case, we want to get every output
            out.append(curr)
            for i in range(start, len(nums)):
                # make decision
                curr.append(nums[i])
                # recursive
                backtrack(nums, out, curr, start+1)
                # undo decision
                curr.pop()











# vN3cDgqs

