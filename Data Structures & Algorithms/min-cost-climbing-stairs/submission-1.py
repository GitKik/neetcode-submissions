class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2 :
            return min(cost)
        prev_prev = cost[0]
        prev = cost[1]
        cost_return = [prev_prev, prev]
        for i in range(2, len(cost)) :
            cost_return.append(cost[i] + min(prev_prev, prev))
            prev_prev = cost_return[i-1]
            prev = cost_return[i]
        return min(cost_return[-2], cost_return[-1])
        