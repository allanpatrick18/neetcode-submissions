class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for ele in nums:
            counter[ele] = counter.get(ele, 0) + 1
            if counter[ele] > len(nums)/2:
                return ele
