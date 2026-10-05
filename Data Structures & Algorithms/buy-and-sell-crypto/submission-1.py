class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]

        for price in prices:
            if price > low:
                res = max(res, price-low)
            else:
                low = price
        
        return res