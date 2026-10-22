
class Solution:
    def decomposeTarget(self, 
                        target: int, 
                        decomposition: tuple[int, ...],
                        nums: list[int],
                        decompo_sum: int) -> list[tuple[int]] :
        if decompo_sum == target :
            return [tuple(decomposition)]
        if decompo_sum > target :
            return [tuple()]
        else :
            first = nums[0]
            decomposition_added = (*decomposition, first)
            if len(nums) == 1 :
                return self.decomposeTarget(target, decomposition_added, nums, decompo_sum + first)
            
            return (self.decomposeTarget(target, decomposition, nums[1:], decompo_sum)
                    + self.decomposeTarget(target, decomposition_added, nums, decompo_sum + first))
    
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        decompo_fat = self.decomposeTarget(target, tuple() ,sorted(nums), 0)
        return [list(x) for x in decompo_fat if x]
