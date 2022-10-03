# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        level = 0
        queue = deque([root,])
        
        while queue:
            res.append([])
            level_len = len(queue)
            
            for i in range(level_len):
                node = queue.popleft()
                res[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            level+=1
        
        return res
            
            
            
            
        