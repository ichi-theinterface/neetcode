from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_pointer = 0
        sell_pointer = 1
        profit = 0
        for price in prices:
            while sell_pointer < len(prices):
                if (prices[sell_pointer] - price) > profit:
                    profit = prices[sell_pointer] - price
                    # print(f"buy is {price}, and sell is {prices[sell_pointer]}")
                sell_pointer += 1
            buy_pointer += 1
            sell_pointer = buy_pointer + 1

        return profit

prices = [7,6,4,3,1]

solution = Solution()

print(solution.maxProfit(prices=prices))