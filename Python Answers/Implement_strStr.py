# Author: Shawn Jin
#
# Runtime: 24 ms, faster than 96.35% of Python3 online submissions for Implement strStr().
# Memory Usage: 14 MB, less than 56.73% of Python3 online submissions for Implement strStr().
# 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        # only lower cases
        len_ans = 0
        for i in range(len(haystack)-len(needle)+1):
            len_ans = 0
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                len_ans+=1
            print('j',j)
            if len(needle) == len_ans:
                return i
        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.strStr("a", "a"))