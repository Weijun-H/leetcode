class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        buy = prices[0]  # 储存买入价格
        profit = 0  # 储存利润
        for i in range(1, len(prices)):
            buy = min(buy, prices[i])
            res = prices[i] - buy
            profit = max(res, profit)
        return profit
