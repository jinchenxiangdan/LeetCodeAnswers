class MyHashSet:
    '''
    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity   = 0.8
        self.size       = 0
        self.space      = 10
        self.hashSet    = [None] * self.space
        
        

    def add(self, key: int) -> None:
        # if the space is over used
        if self.size / self.space >= self.capacity:
            # double size the hash set 
            new_space = self.space<<1
            new_set = [None] * new_space
            # move elements to new set
            


    def hashkey(self, key: int) -> int:
        return key % self.space


    def remove(self, key: int) -> None:
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)