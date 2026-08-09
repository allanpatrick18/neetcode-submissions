class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        dub = set()
        for i in range(0,len(nums)):
            if nums[i] in dub:
                return nums[i]
            dub.add(nums[i])

        return nums[-1]