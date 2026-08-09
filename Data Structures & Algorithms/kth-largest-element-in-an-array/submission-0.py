class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
       # Solution 1 
       #  order and the list

       nums.sort()
       return nums[len(nums) - k]