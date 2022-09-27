# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l = root.left
        left_levels = 1
        while(l):
            l = l.left
            left_levels += 1
        r = root.right
        right_levels = 1
        while(r):
            r = r.right
            right_levels += 1
        if left_levels == right_levels:
            return 2** left_levels - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        

        
        
        

        