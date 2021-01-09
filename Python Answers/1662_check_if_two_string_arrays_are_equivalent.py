from typing import List
"""
Author: Shawn Jin

"""

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        This method effiency is close to the easiest way shown below
        """
        input_string_1 = "".join(word1)
        length = len(input_string_1)
        index = 0
        for i in range(len(word2)):
            for char in word2[i]:
                if (index >= length or input_string_1[index] != char):
                    return False
                else:
                    index+=1
        return index == len(input_string_1)

    def arrayStringsAreEqual2(self, word1: List[str], word2: List[str]) -> bool:
        """
        Easiest way to compare the two list of string
        """
        input_string_1 = "".join(word1)
        input_string_2 = "".join(word2)
        return input_string_1 ==  input_string_2


if __name__ == "__main__":
    print(Solution().arrayStringsAreEqual(["ab", "c"], ["a", "bce"]))
