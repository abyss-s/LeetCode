class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 10 ** 12
        dp = [0] + [INF] * amount
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        return dp[amount] if dp[amount] != INF else -1