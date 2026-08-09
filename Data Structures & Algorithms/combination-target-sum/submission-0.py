class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, subset, sumtotal):
            if sumtotal == target:
                res.append(subset.copy())
                return

            if index >= len(nums) or sumtotal > target:
                 return 
            
            subset.append(nums[index])
            dfs(index, subset, sumtotal + nums[index])
            subset.pop()
            dfs(index + 1, subset, sumtotal)
            return 
        
        dfs(0, [], 0)
        return res
