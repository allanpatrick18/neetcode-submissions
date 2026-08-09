class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        posfix = [1] * (len(nums) + 1)
        res = [1] * (len(nums))

        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]

        print(prefix)
        for i in range(len(nums) - 1, 0, -1):
            posfix[i] = posfix[i+1] * nums[i]

        print(posfix)

        for i in range(len(nums)):
            res[i] = prefix[i] * posfix[i+1]
        print(res)
        return res