
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dict__ = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word in self.__dict__:
            return
        self.__dict__[word] = 1
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if word in self.__dict__.keys():
            return True
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == "__main__":
    w = WordDictionary()
    w.addWord('test')
    x = w.search('test')    
    print(x)

