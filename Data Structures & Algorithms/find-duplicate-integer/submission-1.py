class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        pointer_ = nums[0]
        while pointer_ > 0 :
            new_pointer_ = nums[pointer_]
            if new_pointer_ == -1 :
                return pointer_
            else :
                nums[pointer_] = -1
                pointer_ = new_pointer_