# First algo using max (might timout)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        value_map = dict()
        key_set = set()
        out_ = list()
        for i in range(0,k):
            v = nums[i]
            if v not in value_map :
                value_map[v] = 1
                key_set.add(v)
            else :
                value_map[v] += 1 
        key_max = max(key_set)
        out_.append(key_max)
        for i in range(k, len(nums)):
            added = nums[i]
            if added > key_max :
                key_max = added
            if added not in value_map :
                value_map[added] = 0
            value_map[added] += 1 
            key_set.add(added)
            removed = nums[i-k]
            value_map[removed] -= 1 
            if value_map[removed] == 0 :
                key_set.remove(removed)
                if removed == key_max :
                    key_max = max(key_set)
            out_.append(key_max)
        return out_