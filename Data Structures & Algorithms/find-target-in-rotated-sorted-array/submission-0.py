class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        l = 0

        while  l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                return m

            # left position
            if nums[l] <= nums[m]:
                if target > nums[m] or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target >  nums[r]:
                    r =  m - 1
                else:
                    l =  m + 1

        return - 1

