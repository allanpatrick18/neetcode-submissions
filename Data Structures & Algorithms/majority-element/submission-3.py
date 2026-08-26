class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter = {}
        # for ele in nums:
        #     counter[ele] = counter.get(ele, 0) + 1
        #     if counter[ele] > len(nums)/2:
        #         return ele

        counter, res = 1, nums[0]
        for n in nums[1::]:
            if res == n:
                counter +=1
            elif counter > 0:
                counter -=1
            else:
                res = n
        
        return res
            
            