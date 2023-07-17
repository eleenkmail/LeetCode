class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit , minimum = 0, prices[0]

        for i in range(len(prices)):

            minimum = min(prices[i], minimum)
            profit = max(profit, (prices[i] - minimum))
            
        

        return profit

      


            