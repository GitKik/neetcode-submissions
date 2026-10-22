class Solution:

    def pick(self, nums:List[int], current_num:List[int]):
        if len(nums) == 1 :
            return [current_num + nums]
        else :
            temp = []
            for i in range(len(nums)) :
                temp += self.pick(nums[:i] + nums[i+1:], current_num + [nums[i]])
            return temp
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Pick one number then another etc until you have all numbers
        
        return self.pick(nums, [])

