# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # res = dict()

        # def dfs(root):
        #     nonlocal res
        #     if root == None:
        #         return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     if left not in res:
        #         res[left] = [root.val]
        #     else:
        #         res[left].append(root.val)

            
        #     return 1 + max(left,right)
        
        # dfs(root)
        # print(res)
        # f = []
        # for k, v  in res.items():
        #     f.append(v)
        # print(f)
        # return f


        q = deque()
        res = []
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
                
                
        return res

