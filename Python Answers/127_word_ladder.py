#!/usr/bin/python3
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Author: Shawn Jin
        Precondition:
            1 <= beginWord.length <= 100
            endWord.length == beginWord.length
            1 <= wordList.length <= 5000
            wordList[i].length == beginWord.length
            beginWord, endWord, and wordList[i] consist of lowercase English letters.
            beginWord != endWord
            All the strings in wordList are unique.
        """
        
        # The endWord is not in wordList, therefore no possible transformation.
        if endWord not in wordList:
            return 0

        # the endWord is in wordList, finding the shortest path
        self.EMPTY = -1
        checkPool = []
        self.shortestPathLength = self.EMPTY


        def couldConvert(lastWord: str, targetWord: str) -> bool:
            """
            Check if the two string only have specific number of characters are different.
            Default difference is { 1 }
            """
            # set the difference char
            REQUIRE_DIFF = 1
            # comparing
            if (len(lastWord) != len(targetWord)):
                return False
            
            total_diff = 0
            for i in range(len(targetWord)):
                if (targetWord[i] != lastWord[i]):
                    total_diff += 1
            return total_diff == REQUIRE_DIFF



        def helper(lastWord, targetWord, checkPool, wordList):
            
            if lastWord == targetWord:
                print("find the same one!")
                if ((self.shortestPathLength == self.EMPTY 
                        or len(checkPool) < self.shortestPathLength)):
                    print(checkPool)
                    self.shortestPathLength = len(checkPool)
                return
            
            for word in wordList:
                if (word not in checkPool 
                        and couldConvert(lastWord, word)):
                    print(lastWord, "--got in the loop:", word)
                    checkPool.append(word)
                    helper(word, targetWord, checkPool, wordList)
                    checkPool.remove(word)

        helper(beginWord, endWord, checkPool, wordList)
        # return self.shortestPathLength if beginWord in wordList else self.shortestPathLength+1
        return self.shortestPathLength + 1

if __name__ == "__main__":
    S = Solution()
    print("----------")
    # print(S.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    # print(S.ladderLength("a", "c", ["a", "b", "c"]))
    print(S.ladderLength("leet","code", ["lest","leet","lose","code","lode","robe","lost"]))
