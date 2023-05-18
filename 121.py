class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_pointer = 0
        right_pointer = 1
        max_profit = 0

        # loop through the prices array
        while right_pointer < len(prices):
            current_profit = prices[right_pointer] - prices[left_pointer]

            # if prices left is less than right, we know it is going to be a profit
            if prices[left_pointer] < prices[right_pointer]:
                max_profit = max(max_profit, current_profit)

            # otherwise, move left pointer to right and increment right_pointer
            else:
                left_pointer = right_pointer

            right_pointer += 1

        return max_profit
