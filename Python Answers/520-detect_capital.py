class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        '''
        Rules:
            All letters in this word are capitals, like "USA".
            All letters in this word are not capitals, like "leetcode".
            Only the first letter in this word is capital, like "Google".
        '''
        if word is None:
            return  False
        if len(word) < 2:
            return True
        # check all False cases
        if word[0].isupper():
            if word[1] and word[1].isupper():
                for i in range(2, len(word)):
                    # check all False cases
                    if word[i].islower():
                        return False
                return True
            else: # is lower
                for i in range(2, len(word)):
                    if word[i].isupper():
                        return False
                return True
        else:
            # the first char is lower case 
            for char in word:
                if char.isupper():
                    return False
            return True
