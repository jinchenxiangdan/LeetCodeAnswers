from typing import List
# Pascal's Triangle II
# 
# Author: Shawn Jin
# Runtime beats 85.27% of python3 submissions
#

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        temp = [1]
        out = [1,1]
        if rowIndex == 0:
            return temp
        elif rowIndex == 1:
            return out
        else:
            # rowindex >= 2
            while (len(out)-1 < rowIndex):
                temp = [0] * (len(out)+1)
                length = len(temp)
                temp[0] = 1
                temp[-1] = 1
                range_max = int(length / 2) if length % 2 == 0 else int(length/2)+1
                for i in range(1, range_max):
                    print('i',i)
                    temp[i] = out[i-1] + out[i]
                    temp[-i-1] = temp[i]
                out = temp
                print('out', out)
        return out

#
# testing 
#
if __name__ == "__main__":
    
    s = Solution()
    print(s.getRow(6))
    