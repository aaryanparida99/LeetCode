# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def compute_depth(self,node):
        d = 0
        while node.left:
            node = node.left
            d+=1
        return d
    
    def exist(self,index,depth,node):
        left , right = 1 , 2**depth 
        for i in range(depth):
            mid = left + (right -left) // 2
            if index <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = self.compute_depth(root)
        if depth == 0:
            return 1
        
        
        left,right = 1 , 2**depth 
        while(left<=right):
            mid =  left + (right-left)//2
            if self.exist(mid,depth,root):
                left = mid + 1
            else:
                right = mid - 1
                
        return (2**depth-1) + left - 1

        
        
        

        