# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count_good = 0
        max_val = float("-inf")
        def dfs(root, max_val):
            nonlocal count_good
            if not root:
                return
            
            max_val = max(root.val,max_val)
            if max_val == root.val:
                count_good += 1
            dfs(root.left,max_val)
            dfs(root.right,max_val)

        
        dfs(root,max_val)
        return count_good
            
        