# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, 
                 root: Optional[TreeNode], 
                 subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None :
            return True
        if root is None :
            return False
        
        if self.treeEquals(root, subRoot) :
            return True
        else :
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def treeEquals(self, tree_1: TreeNode, tree_2: TreeNode) -> bool :
        if any(x is None for x in [tree_1, tree_2]): 
            if (tree_1 is None) and (tree_2 is None) :
                return True
            return False
        
        if tree_1.val == tree_2.val :
            return self.treeEquals(tree_1.left, tree_2.left) and self.treeEquals(tree_1.right, tree_2.right)
        return False 