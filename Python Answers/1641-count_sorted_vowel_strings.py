from typing import List

def countVowelStrings_O1(self, n: int) -> int:
    """
    Author: Shawn Jin
    O(1) method
    """
    #return comb(n+4, 4)
    return (n + 1) * (n + 2) * (n + 3) * (n + 4) / 24
    
def countVowelStrings_On(self, n: int)