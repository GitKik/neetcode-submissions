# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        all_children_l = self.getAllChildren(root.left)
        all_children_r = self.getAllChildren(root.right)
        if (p.val in all_children_l) and (q.val in all_children_l) :
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val in all_children_r) and (q.val in all_children_r) :
            return self.lowestCommonAncestor(root.right, p, q)
        else :
            return root


    def getAllChildren(self, root: TreeNode) -> list:
        if (root is None) :
            return [] 
        return [root.val] + self.getAllChildren(root.left) + self.getAllChildren(root.right)