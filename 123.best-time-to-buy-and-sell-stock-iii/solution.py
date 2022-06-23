"""
#
# (1) Backtracking approach (You will get a TLE error)
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        N = len(prices)
        def backtracking(idx: int, buy: int, isHolding: int, remainCnt: int) -> int:

            if (idx == N):
                return 0

            if (buy & 1 == 0):
                return max(
                    # case : we don't buy a stock
                    backtracking(idx + 1, buy, isHolding, remainCnt),

                    # case : we buy a stock
                    backtracking(idx + 1, prices[idx], 1, remainCnt - 1) if (remainCnt > 0) else 0
                )
            else:
                # print("{} : buy at {}, remain:{}".format(idx, buy, remainCnt))
                return max(
                    # case : we don't sell the holding stock
                    backtracking(idx + 1, buy, isHolding, remainCnt),

                    # case : we sell the holding stock
                    backtracking(idx + 1, 0, 0, remainCnt) + prices[idx] - buy
                )


        return backtracking(0, 0, 2)
"""

"""
#
# (2) Optimize the backtracking approach
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        N = len(prices)
        def backtracking(idx: int, isHolding: int, remainCnt: int) -> int:

            if (idx == N) or (remainCnt == -1):
                return 0

            if (isHolding == 0):
                return max(
                    # case : we don't buy a stock
                    backtracking(idx + 1, isHolding, remainCnt),

                    # case : we buy a stock
                    -prices[idx] + backtracking(idx + 1,  1, remainCnt - 1)
                )
            else:
                # print("{} : buy at {}, remain:{}".format(idx, buy, remainCnt))
                return max(
                    # case : we don't sell the holding stock
                    backtracking(idx + 1, isHolding, remainCnt),

                    # case : we sell the holding stock
                    backtracking(idx + 1, 0, remainCnt) + prices[idx]
                )


        return backtracking(0, 0, 2)
"""
