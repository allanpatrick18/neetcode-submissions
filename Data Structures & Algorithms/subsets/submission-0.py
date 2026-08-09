class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        subset = []
        
        def dfs(i):
            if i >= len(nums):
                print(i)
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            print(i)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res