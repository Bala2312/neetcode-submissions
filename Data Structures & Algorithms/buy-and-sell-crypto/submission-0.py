class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            for j in range(len(prices)):
                if j > i:
                    sum = prices[j] - prices[i]
                    if sum > max:
                        max = sum
        return max