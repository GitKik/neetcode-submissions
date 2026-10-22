class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        needed_to_end = 1
        possible = False
        nums.reverse()
        for n in nums[1:]:
            if n >= needed_to_end:
                needed_to_end = 1
                possible = True
            else :
                needed_to_end += 1
                possible = False
        return possible
            