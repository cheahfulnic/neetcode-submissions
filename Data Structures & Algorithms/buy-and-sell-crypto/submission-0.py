class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runningPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if price > runningPrice:
                diff = price - runningPrice
                if diff > maxProfit:
                    maxProfit = diff
            else:
                runningPrice = price
        return maxProfit
            