class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0



        buy_index = 0
        sell_index = len(prices) - 1


        while buy_index < sell_index:
            diff = prices[sell_index] - prices[buy_index]
            if diff > max_profit:
                max_profit = diff
            
            buy_index += 1

            if buy_index == sell_index:
                buy_index = 0
                sell_index -= 1



        return max_profit