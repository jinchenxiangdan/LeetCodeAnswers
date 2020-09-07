from typing import List
'''
Best Time to Buy and Sell Stock III
'''

# class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
        # return 1


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        output = [0]*num_people
        curr_candies = candies
        curr_cost = 1

        while curr_candies > 0:
            for i in range(num_people):
                if curr_candies - curr_cost > 0:
                    output[i] += curr_cost
                    curr_candies -= curr_cost
                    curr_cost+=1
                else:
                    output[i] += curr_candies
                    return output
        return output


if __name__ == "__main__":
    stock1 = [3,3,5,0,0,3,1,4]
    # using enumeration, but it takes lots of time and memory

    x = stock1.remove(3)
    res = list(filter(lambda a : a  != '', stock1))
    print(res)

    print(stock1)