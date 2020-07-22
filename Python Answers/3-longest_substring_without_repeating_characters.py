class Solution:
    '''
    This method using a list to store the longest substring

    Runtime: 88 ms, faster than 42.58% of Python3 online submissions for Longest Substring Without
    Repeating Characters.
    Memory Usage: 14 MB, less than 50.82% of Python3 online submissions for Longest Substring 
    Without Repeating Characters.
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if input is none, then return none
        if s is None:
            return 0
        # check the output 
        ans = 0
        curr = []
        for c in s:
            if c not in curr:
                pass
            else:
                if len(curr) > ans:
                    ans = len(curr)
                curr = curr[curr.index(c)+1:]
            curr.append(c)
        return max(ans, len(curr))

    '''
    This method used a string to represent the longest string

    Runtime: 48 ms, faster than 96.46% of Python3 online submissions for Longest Substring Without 
    Repeating Characters.
    Memory Usage: 13.9 MB, less than 60.26% of Python3 online submissions for Longest Substring 
    Without Repeating Characters.
    '''
    def lengthOfLongestSubstring_fast(self, s: str) -> int:
        if len(s) == 0:
            return 0
        temp = s[0]
        max_len = 1
        for letter in s[1:]:
            if letter in temp:
                i = temp.find(letter)
                temp = temp [i+1:]
            temp += letter
            if len(temp) > max_len:
                max_len = len(temp)
        return max_len
    