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
