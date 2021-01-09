from typing import List

class Solution:
    #
    # Using a helper function
    #
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def get_combination(answers, candidates, temp, target, start_index):
            if ( sum(temp) == target ):
                print("sum:",sum(temp))
                answers.append(temp.copy())
            elif ( sum(temp) > target ):
                return
            else:
                for i in range(start_index, len(candidates)):
                    temp.append(candidates[i])
                    get_combination(answers, candidates, temp, target, i)
                    temp.pop(-1)
        
        answers = []
        get_combination(answers, candidates, [] ,target, 0)
        
        print(answers)
        return answers





#
# Test Area
#
if __name__ == "__main__":
    s = Solution()
    s.combinationSum([2,3,6,7], 7)
    # print(s.combinationSum([2,2,3,7], 7))

