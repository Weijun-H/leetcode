class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        n = len(prices)
        if n <= 1:
            return max_profit
        index = 1
        valley = peak = prices[0]
        while index < n:
            while index < n and prices[index] < prices[index-1]:        # 查找谷底
                index += 1
            valley = prices[index-1]
            while index < n and prices[index] > prices[index-1]:        # 查找山峰
                index += 1
            peak = prices[index-1]
            max_profit += peak - valley
        return max_profit