'''
Author: Shawn Jin
'''
import collections
from typing import List 

class Solution:
    '''
    Runtime: 136 ms, faster than 33.83% of Python3 online submissions for Top K Frequent Elements.
    Memory Usage: 18.4 MB, less than 17.97% of Python3 online submissions for Top K Frequent Elements.
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_hashtable = {}
        for item in nums:
            if item in my_hashtable:
                my_hashtable[item] += 1
            else:
                my_hashtable[item] = 1
        sorted_hashtable = sorted(my_hashtable.items(), key=lambda item: item[1], reverse=True)
        return [sorted_hashtable[i][0] for i in range(k)]

    '''
    Runtime: 136 ms, faster than 33.83% of Python3 online submissions for Top K Frequent Elements.
    Memory Usage: 18.4 MB, less than 24.68% of Python3 online submissions for Top K Frequent Elements.
    '''
    def topKFrequent_oneLine(self, nums: List[int], k: int) -> List[int]:
        return [x for x,_ in sorted(collections.Counter(nums).items(), key=lambda x:-x[1])[:k]]