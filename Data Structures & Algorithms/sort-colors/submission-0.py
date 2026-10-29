class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red_ptr = 0
        blue_ptr = len(nums) - 1
        for n in nums :
            if n==0:
                red_ptr += 1 
            elif n==2:
                blue_ptr -= 1
        for i in range(len(nums)):
            if i < red_ptr:
                nums[i] = 0
            elif i > blue_ptr :
                nums[i] = 2
            else :
                nums[i] = 1
        return nums