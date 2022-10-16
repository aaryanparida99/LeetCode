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
            level_len = len(queue)
            subres = []
            for i in range(level_len):
                node = queue.popleft()
                subres.append(node.val)             
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(subres)
            level += 1
        return res
            
            
            
            
        