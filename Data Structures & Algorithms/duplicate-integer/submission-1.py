class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hash_map = set()
        for n in nums:
            hash_map.add(n)
    
        
        return True if len(hash_map) < len(nums) else False