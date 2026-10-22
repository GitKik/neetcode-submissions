# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from heapq import *

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        print('INNN')
        nodes_to_explore = [root] if root.val else []
        all_values = []
        heapq.heapify(all_values)
        while nodes_to_explore :
            temp_node = []
            for node in nodes_to_explore :
                if node.val :
                   heapq.heappush(all_values, node.val)
                   temp_node += [x for x in [node.left, node.right] if x is not None]
            nodes_to_explore = temp_node
        print(all_values)
        for k_ in range(1,k):
            heapq.heappop(all_values)
        print(all_values)
        return heapq.heappop(all_values)