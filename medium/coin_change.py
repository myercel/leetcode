"""
Problem No. 322

You are given an integer array coins representing coins of 
different denominations and an integer amount representing 
a total amount of money.
Return the fewest number of coins that you need to make up 
that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:
    Input: coins = [1,2,5], amount = 11
    Output: 3
    Explanation: 11 = 5 + 5 + 1
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dynamic Programming - repeated subproblems 
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        
        if dp[amount] != (amount + 1):
            return dp[amount]

        return -1

        """
        if not coins or not amount:
            return -1

        coins.sort(reverse = True)
        i = 0
        count = 0

        while i < len(coins) and amount >= 0:
            if amount > i:
                amount -= i
                count += 1
            else:
                i += 1

        if count:
            return count
        return -1
        """