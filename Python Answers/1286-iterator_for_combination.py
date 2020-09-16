class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.conbinations = []

        def find_combination(characters, length, start, output: str):
            # base case 
            if length == 0:
                self.conbinations.append(output)
                return
            # use a for loop to combine answers 
            for i in range(start, len(characters)):
                output += characters[i]
                find_combination(characters, length-1, i+1, output)
                output = output[:-1]

        find_combination(characters, combinationLength, 0, "")

    def next(self) -> str:
        return self.conbinations.pop(0)

    def hasNext(self) -> bool:
        return self.conbinations


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
