'''
Author: Shawn Jin
Runtime beats 92.13% of Python3 submissions
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        for index in range(len(s)):
            power = 26 ** index
            position = len(s)-index-1
            total += (ord(s[position])-64)*power
        return total
