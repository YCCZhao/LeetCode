"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        counter = 1
        top = -1
        temp = 1

        for i in range(1,len(ratings)):
            if ratings[i] < ratings[i-1]:
                counter += i-top
                if top >0 and top_candy <=  i-top:
                    counter += 1
                temp = 1
            if ratings[i] >= ratings[i-1]:
                if ratings[i] == ratings[i-1]:
                    temp = 1
                if ratings[i] > ratings[i-1]:
                    temp += 1
                counter += temp
                top = i
                top_candy = temp
        return counter   

                
        
