class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        previous_idx = -1
        left, right = 0, len(nums)
        while not found :
            idx_target = (left + right) // 2
            target_ = nums[idx_target]
            if previous_idx == idx_target :
                return -1
            elif target_ == target :
                return idx_target
            elif target < target_ :
                right = idx_target
            else :
                left = idx_target
            previous_idx = idx_target

        