'''
Runtime: 28 ms, faster than 90.22% of Python3 online submissions for Add Digits.
Memory Usage: 13.9 MB, less than 41.04% of Python3 online submissions for Add Digits.
Reference: https://leetcode.com/dbabichev/
'''
class Solution:
    def addDigits(self, num: int) -> int:
        # Theorem For any natural number n: numbers n and sum(n) have the same remainder if we divide them by 9.
        return 0 if num == 0 else (num - 1) % 9 + 1
