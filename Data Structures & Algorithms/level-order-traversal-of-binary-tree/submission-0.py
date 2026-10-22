# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            i = 0
            res = [[root.val]]
            next_ = [ x for x in [root.left, root.right] if x]
            while len(next_) :
                temp_next = []
                res_append = []
                for n in next_ :
                    res_append.append(n.val)
                    temp_next += [ x for x in [n.left, n.right] if x]
                next_ = temp_next
                res.append(res_append)
            return res
        else :
            return []