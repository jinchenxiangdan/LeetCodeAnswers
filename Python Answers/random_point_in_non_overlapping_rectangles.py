import random
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        # self.indexs = self.shuffle_valid_ractangles(self.rects)
        self.indexs = [i for i in range(len(self.rects))]
        random.shuffle(self.indexs)


    def pick(self) -> List[int]:
        if not self.indexs:
            # self.indexs = self.shuffle_valid_ractangles(self.rects)
            random.shuffle(self.indexs)
        index = self.indexs.pop()
        rect = self.rects[index]
        # print('r',rect)
        x_min = min(rect[0], rect[2])
        x_max = max(rect[0], rect[2])
        y_min = min(rect[1], rect[3])
        y_max = max(rect[1], rect[3])
        return [random.randint(x_min, x_max), random.randint(y_min, y_max)]
        

    # def shuffle_valid_ractangles(self, rects):
    #     output = []
    #     for i in range(len(rects)):
    #         if rects[i]:
    #             output.append(i)
    #     random.shuffle(output)
    #     return output


# Your Solution object will be instantiated and called as such:
rects = [[-2,-2,-1,-1],[1,0,3,0]]
obj = Solution(rects)
print( obj.pick())



[[-2,-2,-1,-1],[1,0,3,0]]

[],[],[],[],[]