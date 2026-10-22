class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        matches = []
        nums.sort()
        if len(nums) < 3 :
            return matches
        for idx_target in range(len(nums)-2) :
            target = - nums[idx_target] 
            l = idx_target+1
            r = len(nums)-1 
            while l < r :
                if nums[l] + nums[r] == target :
                    success_3_nums = [-target, nums[l], nums[r]]
                    if success_3_nums not in matches:
                        matches.append(success_3_nums)
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > target :
                    r -= 1
                else :
                    l +=1
        return matches 