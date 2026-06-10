# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        
        res = []
        q.append(root)

        while q:
            size = len(q)
            level_list = []
            for _ in range(size):
                cur_node = q.popleft()
                level_list.append(cur_node.val)

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            res.append(level_list)


        
        return res

