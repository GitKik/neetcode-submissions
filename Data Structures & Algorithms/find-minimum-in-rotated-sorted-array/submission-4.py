class Solution:
    def findMin(self, nums: List[int]) -> int:
        idx_l, idx_r = 0, len(nums) - 1
        l,r = nums[idx_l], nums[idx_r]
        
        while l != r:
            idx_m = (idx_l + idx_r) // 2
            m = nums[idx_m]
            print("idx_l : ",idx_l, " = ",l,
                  "idx_m : ",idx_m, " = ",m,
                  "idx_r :", idx_r," = ",r) 

            if (m ==r)  or (m==l):
                return min(r,l)

            if m > r :
                idx_l = idx_m
            elif m < r :
                idx_r = idx_m
            
            l,r = nums[idx_l], nums[idx_r]
        return r