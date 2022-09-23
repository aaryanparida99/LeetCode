# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.res.append(root.val)
            self.inorder(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.res = []   
        if root is None:
            return True
        else:
            self.inorder(root)
        n = len(self.res)
        for i in range(0,n-1):
            if self.res[i] >= self.res[i+1]:
                return False
        return True
        

        