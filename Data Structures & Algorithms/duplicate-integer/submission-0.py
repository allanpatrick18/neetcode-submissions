class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        stack = set() 
        for ele in nums:
            if ele in stack:
                return True
            stack.add(ele)

        return False 