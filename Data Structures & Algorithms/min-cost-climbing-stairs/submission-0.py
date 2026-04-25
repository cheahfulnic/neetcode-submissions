class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_zero, cost_one = cost[0], cost[1]

        for i in range(2, len(cost)):
            current = min(cost_zero, cost_one) + cost[i]
            cost_zero = cost_one
            cost_one = current

        return min(cost_zero, cost_one)