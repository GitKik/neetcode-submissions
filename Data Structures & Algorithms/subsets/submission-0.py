class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets_ = [[]]

        def explore(nums: List[int], current_sub: List[int]):
            if len(nums) == 0:
                return 
            value = nums[0]
            subsets_.append(current_sub + [value])
            explore(nums[1:], current_sub)
            explore(nums[1:], current_sub + [value])

        explore(nums,[])
        return subsets_